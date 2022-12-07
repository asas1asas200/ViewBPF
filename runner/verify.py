import sys
from io import StringIO

from bcc import BPF

if __name__ == '__main__':
	code = ''
	while True:
		try:
			line = input()
		except EOFError:
			break
		code += line + '\n'
	BPF(text=code, debug=0)
