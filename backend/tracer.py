import json
from uuid import uuid4


class Tracer:
	def __init__(self, r, name, program, options, **kwargs):
		self.r = r
		self.name = name
		self.program = program
		self.options = options
		while True:
			self.key = str(uuid4())
			if not self.r.exists(self.key):
				break
		self.r.rpush('programs', json.dumps({'name': self.name, 'key': self.key}))
