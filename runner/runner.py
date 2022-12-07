import json
from uuid import uuid4
from subprocess import Popen, PIPE


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
		self.r.rpush(self.key, json.dumps(data))

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