from flask import Flask
from flask_cors import CORS

from routes.example import example

app = Flask(__name__)

CORS(app, resources={r'/api/*': {'origins': '*'}})


@app.route('/api/ping')
def ping():
    return "received ping"


@app.route('/')
def hello_world():
	return '<p>Hello, World!</p>'


app.register_blueprint(example, url_prefix='/api/example')
