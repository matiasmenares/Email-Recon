import socket
import smtplib
import dns.resolver
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-m", help="Email")

params = parser.parse_args()

email = params.m
domain = email.split("@")

answers = dns.resolver.query(domain[1], 'MX')
for rdata in answers:
	mxx = rdata.exchange

host = socket.gethostname()
# SMTP lib setup (use debug level for full output)
server = smtplib.SMTP()
server.set_debuglevel(0)
# SMTP Conversation
server.connect(str(mxx))
server.helo(str(domain[1]))
server.mail(email)
code, message = server.rcpt(str(email))
server.quit()

# Assume 250 as Success
if code == 250:
	print('Verdadero')
else:
	print('Falso')