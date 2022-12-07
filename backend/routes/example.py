import json
from flask import Blueprint, request
import pika
from ..model import r


example = Blueprint('example', __name__)


@example.route('/test')
def test():
	return "GET /api/example/test"


@example.route('/simple_http_parse', methods=['POST'])
def simpleHttpParse():
	data = request.get_json()
	connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
	channel = connection.channel()
	channel.queue_declare(queue='program')
	channel.basic_publish(
		exchange='', routing_key='program', body=json.dumps(data))
	connection.close()
	return f"New program {data['name']} created."
