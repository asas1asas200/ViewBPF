from multiprocessing import Process
import json

from redis import Redis

from examples.http_parse_simple import HttpParseSimple
from examples.disk_snoop import DiskSnoop


def run_program(program):
	program.verify()
	program.build()
	program.run()


if __name__ == '__main__':
	PROGRAM_MAPPING = {
		'Simple HTTP Parse': HttpParseSimple,
		'Disk Snoop': DiskSnoop
	}
	r = Redis(host='localhost', port=6379, db=0, decode_responses=True)
	r.flushall()
	sub = r.pubsub(ignore_subscribe_messages=True)
	sub.subscribe('programs')

	print(' [*] Waiting for messages. To exit press CTRL+C')
	for body in sub.listen():
		data = json.loads(body['data'])
		runner = PROGRAM_MAPPING[data['program']](r, **data)
		p = Process(target=run_program, args=(runner,))
		p.start()
