import urllib
import urllib2
from pyquery import PyQuery as pq

linux_url_default = "http://blog.jobbole.com/tag/algorithm/"  # the url
smtp_address = "121.195.178.51:25" # the smtp address 
user = "" # your smtp mailbox
passwd = ""  # password
how_many_page = 8

# pocket 
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
 
# python 2.3.*: email.Utils email.Encoders
from email.utils import COMMASPACE,formatdate
from email import encoders
 
import os
 
#server['name'], server['user'], server['passwd']
def send_mail(server, fro, to, subject, text, files=[]): 
	assert type(server) == dict 
	assert type(to) == list 
	assert type(files) == list 
 
	msg = MIMEMultipart() 
	msg['From'] = fro 
	msg['Subject'] = subject 
	msg['To'] = COMMASPACE.join(to) #COMMASPACE==', ' 
	msg['Date'] = formatdate(localtime=True) 
	msg.attach(MIMEText(text)) 
 
	for file in files: 
		part = MIMEBase('application', 'octet-stream') #'octet-stream': binary data 
		part.set_payload(open(file, 'rb'.read())) 
		encoders.encode_base64(part) 
		part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(file)) 
		msg.attach(part) 
 
	import smtplib 
	smtp = smtplib.SMTP(server['name']) 
	smtp.login(server['user'], server['passwd']) 
	smtp.sendmail(fro, to, msg.as_string()) 
	smtp.close()

server = {}
server["name"] = smtp_address
server["user"] = user
server["passwd"] = passwd

to = []
to.append("add@getpocket.com")

url_list = {}

for i in range(1,how_many_page + 1):  # number of page
	linux_url = linux_url_default + str(i) +"/"

	response = urllib.urlopen(linux_url)
	soup = pq(response.read())

	ass = soup("a.meta-title")

	for a in ass:
		# url_list[a.text.encode("utf-8")] = a.get("href")
		send_mail(server, "laozhikun@163.com", to, "Add", a.get("href"))

# print url_list



