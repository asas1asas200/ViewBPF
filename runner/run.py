from multiprocessing import Process
import json

from redis import Redis

from examples.http_parse_simple import HttpParseSimple
from examples.disk_snoop import DiskSnoop


def run_program(program):
	try:
		program.verify()
		program.build()
		program.run()
	except Exception as e:
		info = json.loads(program.r.get(f'{program.key}:info'))
		info['state'] = 'error'
		info['error_message'] = str(e)
		program.r.set(f'{program.key}:info', json.dumps(info))


if __name__ == '__main__':
	PROGRAM_MAPPING = {
		'Simple HTTP Parse': HttpParseSimple,
		'Disk Snoop': DiskSnoop
	}
	r = Redis(host='localhost', port=6379, db=0, decode_responses=True)
	r.flushall()
	sub = r.pubsub(ignore_subscribe_messages=True)
	sub.subscribe('programs')
	sub.subscribe('stop')

	running_programs = {}

	print(' [*] Waiting for messages. To exit press CTRL+C')
	for body in sub.listen():
		match body['channel']:
			case 'programs':
				data = json.loads(body['data'])
				runner = PROGRAM_MAPPING[data['program']](r, **data)
				p = Process(target=run_program, args=(runner,))
				p.start()
				running_programs[runner.key] = p
			case 'stop':
				key = body['data']['programID']
				running_programs[key].kill()
				info = json.loads(r.get(f'{key}:info'))
				info['state'] = 'finished'
				r.set(f'{key}:info', json.dumps(info))
