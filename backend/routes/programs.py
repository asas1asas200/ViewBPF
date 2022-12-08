import json

from flask import Blueprint

from ..model import r

programs = Blueprint('programs', __name__)


@programs.route('/')
def get_programs():
	return [json.loads(pinfo) for pinfo in r.lrange('programs', 0, -1)] if r.exists('programs') else []


@programs.route('/<key>')
def get_program(key):
	if not r.exists(key + ':info'):
		return 'Not found', 404
	data = json.loads(r.get(key + ':info'))
	return data, 200
