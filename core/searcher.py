import socket
import smtplib
import dns.resolver

class Searcher:

	def __init__(self, email):
		self.email = email
		self.domail = self.get_domain()
		self.mx = self.get_mx_exchange()

	def cut(self,data,delimiter):
		return data.split(delimiter)

	def get_domain(self):
		domain = self.cut(self.email,"@")
		return str(domain[1])

	def get_mx_exchange(self):
		answers = dns.resolver.query(self.domail, 'MX')
		for rdata in answers:
			mxx = rdata.exchange		
		return str(mxx)

	def searcher(self):
		host = socket.gethostname()
		server = smtplib.SMTP()
		server.set_debuglevel(0)
		server.connect(self.mx)
		server.helo(self.domail)
		server.mail(self.email)
		code, message = server.rcpt(str(self.email))
		server.quit()
		if code == 250:
			print('Valid')
		else:
			print('Not Found')