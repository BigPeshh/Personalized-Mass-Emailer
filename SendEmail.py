#This program sends an email to an individual

import smtplib

#Sign into email account
e = input(str("Email Address: "))
p = input(str("Password: "))
r = input(str("Recipient Email: "))
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login(e, p)

#The Email 
msg = "Hello, this is a test email."

#Sending email to recipient
server.sendmail(e, r, msg)
server.quit()
