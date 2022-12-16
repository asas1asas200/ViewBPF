import json

from flask import Blueprint

from model import r

programs = Blueprint('programs', __name__)


@programs.route('/')
def get_programs():
	return [json.loads(pinfo) for pinfo in r.lrange('programs', 0, -1)] if r.exists('programs') else []


@programs.route('/state')
def get_all_programs_state():
	if not r.exists('programs'):
		return {}, 200
	ret = {}
	for program in r.lrange('programs', 0, -1):
		program = json.loads(program)
		ret[program['key']] = json.loads(r.get(f'{program["key"]}:info'))['state']
	return ret, 200


@programs.route('/<key>/stop')
def stop_program(key):
	if not r.exists(f'{key}:info'):
		return 'Not found', 404
	r.publish('stop', json.dumps({'programID': key}))
	return 'OK', 200


@programs.route('/<key>/info')
def get_program_info(key):
	if not r.exists(f'{key}:info'):
		return 'Not found', 404
	data = json.loads(r.get(f'{key}:info'))
	return data, 200


@programs.route('/<key>/verify')
def get_program_verify(key):
	if not r.exists(f'{key}:verify'):
		return 'Not found', 404
	data = r.get(f'{key}:verify')
	return data, 200


@programs.route('/<key>/records')
def get_proggram_records(key):
	if not r.exists(f'{key}:info'):
		return 'Not found', 404
	elif not r.exists(f'{key}:records'):
		return {}, 200
	return [json.loads(record) for record in r.lrange(f'{key}:records', 0, -1)]
