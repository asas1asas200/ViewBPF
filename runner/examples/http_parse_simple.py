import socket
import os

from bcc import BPF

from runner import Runner


class HttpParseSimple(Runner):
	def __init__(self, r, name, program, code, options, **kwargs):
		super().__init__(r, name, program, code)
		self.program = program
		self.interface = options['interface']

	def build(self):
		self.bpf = BPF(text=self.code, debug=0)
		function_http_filter = self.bpf.load_func("http_filter", BPF.SOCKET_FILTER)
		BPF.attach_raw_socket(function_http_filter, self.interface)
		self.socket_fd = function_http_filter.sock
		sock = socket.fromfd(self.socket_fd, socket.PF_PACKET,
								  socket.SOCK_RAW, socket.IPPROTO_IP)
		sock.setblocking(True)

	def run(self):
		while True:
			packet_str = os.read(self.socket_fd, 2048)
			packet_bytearray = bytearray(packet_str)
			ETH_HLEN = 14
			total_length = packet_bytearray[ETH_HLEN + 2]
			total_length = total_length << 8
			total_length = total_length + packet_bytearray[ETH_HLEN + 3]
			ip_header_length = packet_bytearray[ETH_HLEN]
			ip_header_length = ip_header_length & 0x0F
			ip_header_length = ip_header_length << 2
			tcp_header_length = packet_bytearray[ETH_HLEN + ip_header_length + 12]
			tcp_header_length = tcp_header_length & 0xF0
			tcp_header_length = tcp_header_length >> 2
			payload_offset = ETH_HLEN + ip_header_length + tcp_header_length
			for i in range(payload_offset, len(packet_bytearray) - 1):
				if (packet_bytearray[i] == 0x0A):
					if (packet_bytearray[i - 1] == 0x0D):
						break
				print("%c" % chr(packet_bytearray[i]), end="")
			print("")
