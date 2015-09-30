import smtplib
from getpass import getpass

def sendMail(user, password, sendto, msg):
	# determine account
	if user == 'u':
		user =  'jack.sarick@ucc.on.ca'
	else:
		user = 'jacksarick@gmail.com'

	#connect to server
	server = smtplib.SMTP('smtp.gmail.com:587')
	server.starttls()
	server.login(user,password)
	#send and quit
	server.sendmail(user, sendto, msg)
	server.quit()

sendMail(raw_input("User: "), getpass("Password:"), raw_input("Recipient: "), raw_input("Message: "))