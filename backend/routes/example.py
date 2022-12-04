from flask import Blueprint

example = Blueprint('example', __name__)


@example.route('/test')
def test():
	return "GET /api/example/test"
