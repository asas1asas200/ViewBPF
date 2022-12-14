from flask import Flask, request
from flask_cors import CORS
from flask_socketio import SocketIO

from model import r
from routes.example import example
from routes.programs import programs

app = Flask(__name__)

CORS(app, resources={r'/api/*': {'origins': '*'}})

socketio = SocketIO(app, cors_allowed_origins='*')


@app.route('/api/ping')
def ping():
	return "received ping"


@app.route('/')
def hello_world():
	return '<p>Hello, World!</p>'


# Not RESTful but it's a quick hack
@programs.route('/<key>/update')
def update_program(key):
	if not r.exists(f'{key}:info'):
		return 'Not found', 404
	socketio.emit(f'{key}/update')
	return 'OK', 200


app.register_blueprint(example, url_prefix='/api/example')
app.register_blueprint(programs, url_prefix='/api/programs')

if __name__ == '__main__':
	socketio.run(app, host='127.0.0.1', port=5000, debug=True)
