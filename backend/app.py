import json

from flask import Flask
from flask_cors import CORS

from .model import r
from .routes.example import example
from .routes.programs import programs

app = Flask(__name__)


CORS(app, resources={r'/api/*': {'origins': '*'}})


@app.route('/api/ping')
def ping():
	return "received ping"


@app.route('/')
def hello_world():
	return '<p>Hello, World!</p>'


app.register_blueprint(example, url_prefix='/api/example')
app.register_blueprint(programs, url_prefix='/api/programs')
