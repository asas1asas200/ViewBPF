import json
from uuid import uuid4


class Runner:
	def __init__(self, r, name, program):
		self.r = r
		self.name = name
		self.program = program
		while True:
			self.key = str(uuid4())
			if not self.r.exists(self.key):
				break
		self.r.rpush('programs', json.dumps({'name': self.name, 'key': self.key}))

	def log(self, data):
		self.r.rpush(self.key, json.dumps(data))

	def build(self):
		raise NotImplementedError

	def run(self):
		raise NotImplementedError
