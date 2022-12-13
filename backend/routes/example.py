import json
from flask import Blueprint, request
from model import r


example = Blueprint('example', __name__)


@example.route('/test')
def test():
	return "GET /api/example/test"


@example.route('/simple_http_parse', methods=['POST'])
def simpleHttpParse():
	data = request.get_json()
	r.publish('programs', json.dumps(data))
	return f"New program {data['name']} created."
