import json
from uuid import uuid4
from datetime import datetime
from subprocess import Popen, PIPE
from requests import get as requests_get


class Runner:
	def __init__(self, r, name, program, code):
		self.r = r
		self.name = name
		self.program = program
		self.code = code
		while True:
			self.key = str(uuid4())
			if not self.r.exists(self.key):
				break
		self.r.rpush('programs', json.dumps({'name': self.name, 'key': self.key}))
		self.r.set(self.key + ':info', json.dumps(
			{'name': self.name, 'program': self.program, 'code': self.code}))

	def log(self, data):
		data['time'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
		self.r.rpush(self.key + ':records', json.dumps(data))
		# TODO: use async
		requests_get(f'http://localhost:5000/api/programs/{self.key}/update')

	def verify(self):
		p = Popen(['python3', 'verify.py'], stdin=PIPE, stdout=PIPE, stderr=PIPE)
		stdout, stderr = p.communicate(input=self.code.encode('utf-8'))
		p.wait()
		self.verify_result = stderr.decode('utf-8')
		self.r.set(self.key + ':verify', self.verify_result)
		return p.returncode

	def build(self):
		raise NotImplementedError

	def run(self):
		raise NotImplementedError
