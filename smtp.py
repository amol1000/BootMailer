#!/usr/bin/env python
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders
import time
import os
import sys
import cv2


i=0
netActive=False

while netActive==False and i<500 :
    if os.system("ping -c 1 google.com") == 0:
        netActive=True
    i=i+1
    continue
if i>=50:
    print "Check your Connectivity Papi!"
    sys.exit(0)

fromaddr = "kulkarni.amol.13ce1008@gmail.com"
toaddr = "amol1000.ak@gmail.com"
 
msg = MIMEMultipart()
 
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "PC BOOTED"

localtime=time.asctime(time.localtime(time.time()))
body = "PC Has been started ::"+localtime
 
msg.attach(MIMEText(body, 'plain'))
 
filename = "test.png"
attachment = open("/home/amol/python/test.png", "rb")
 
part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
 
msg.attach(part)
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "honda@dio315")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
