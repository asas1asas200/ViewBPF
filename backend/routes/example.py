from flask import Blueprint, request
from ..tracer import Tracer
from ..model import r

example = Blueprint('example', __name__)


@example.route('/test')
def test():
	return "GET /api/example/test"


@example.route('/simple_http_parse', methods=['POST'])
def simpleHttpParse():
	data = request.get_json()
	print(data)
	tracer = Tracer(r, **data)
	return f"New tracer {data['name']} created."
