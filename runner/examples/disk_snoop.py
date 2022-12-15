from __future__ import print_function

from bcc import BPF

from runner import Runner


class DiskSnoop(Runner):
	REQ_WRITE = 1

	def __init__(self, r, name, program, code, **kwargs):
		super().__init__(r, name, program, code)
		self.program = program

	def build(self):
		self.bpf = BPF(text=self.code, debug=0)

		if BPF.get_kprobe_functions(b'blk_start_request'):
				self.bpf.attach_kprobe(event="blk_start_request", fn_name="trace_start")
		self.bpf.attach_kprobe(event="blk_mq_start_request", fn_name="trace_start")
		if BPF.get_kprobe_functions(b'__blk_account_io_done'):
			self.bpf.attach_kprobe(event="__blk_account_io_done",
			                       fn_name="trace_completion")
		else:
			self.bpf.attach_kprobe(event="blk_account_io_done",
			                       fn_name="trace_completion")

	def run(self):
		while True:
			(task, pid, cpu, flags, ts, msg) = self.bpf.trace_fields()
			(bytes_s, bflags_s, us_s) = msg.split()

			if int(bflags_s, 16) & DiskSnoop.REQ_WRITE:
				type_s = "W"
			elif bytes_s == "0":  # see blk_fill_rwbs() for logic
				type_s = "M"
			else:
				type_s = "R"
			ms = float(int(us_s, 10)) / 1000
			self.log({'data': {'type': type_s, 'lat': ms}})
