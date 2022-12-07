from multiprocessing import Process
import json

import pika
from redis import Redis

from examples.http_parse_simple import HttpParseSimple


def run_program(program):
	program.build()
	program.run()


if __name__ == '__main__':
	PROGRAM_MAPPING = {
		'Simple HTTP Parse': HttpParseSimple,
	}
	r = Redis(host='localhost', port=6379, db=0, decode_responses=True)

	connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
	channel = connection.channel()

	channel.queue_declare(queue='program')

	def callback(ch, method, properties, body):
		data = json.loads(body)
		print(f" [x] Received {data}")
		runner = PROGRAM_MAPPING[data['program']](r, **data)
		p = Process(target=run_program, args=(runner,))
		p.start()

	channel.basic_consume(
		queue='program', on_message_callback=callback, auto_ack=True)

	print(' [*] Waiting for messages. To exit press CTRL+C')
	channel.start_consuming()
