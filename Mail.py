A=input("Enter")
B=input("Enter")
C=input("Enter")
rec=input("Enter the receivers mail address:")

a=f"""Greetings {name},

CONTENT

Var1:{A}
Var2:{B}


Thank You"""

import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

fromaddr = "xyz@gmail.com"
toaddr = rec

msg = MIMEMultipart()

msg['From'] = 'NAME'
msg['To'] = toaddr
msg['Subject'] = "COMPLETED"
body = a

msg.attach(MIMEText(body, 'plain'))

filename = "abc.pdf"
attachment = open("C:\PROGRAMMING\SMTP_PYTHON\abc.pdf", "rb")

p = MIMEBase('application', 'octet-stream')
p.set_payload((attachment).read())
encoders.encode_base64(p)
p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

msg.attach(p)

s = smtplib.SMTP('smtp.gmail.com', 587)

s.starttls()

s.login(fromaddr, "fmlwszthqutdthqb")

text = msg.as_string()

s.sendmail(fromaddr, toaddr, text)

s.quit()
