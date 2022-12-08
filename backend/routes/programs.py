import json

from flask import Blueprint

from ..model import r

programs = Blueprint('programs', __name__)


@programs.route('/')
def get_programs():
	return [json.loads(pinfo) for pinfo in r.lrange('programs', 0, -1)] if r.exists('programs') else []


@programs.route('/<key>/info')
def get_program_info(key):
	if not r.exists(key + ':info'):
		return 'Not found', 404
	data = json.loads(r.get(key + ':info'))
	return data, 200


@programs.route('/<key>/verify')
def get_program_verify(key):
	if not r.exists(key + ':verify'):
		return 'Not found', 404
	data = r.get(key + ':verify')
	return data, 200
