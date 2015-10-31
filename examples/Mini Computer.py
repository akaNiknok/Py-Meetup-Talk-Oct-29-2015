# MINI COMPUTER V2.06
from datetime import datetime
import time

adminpass = "1234567890"
now = datetime.now()
user = "username"
pw = "password"
texts = {}
gallery = []

def reboot():
	print "Rebooting MINI COMPUTER V2.06..."
	admin = raw_input("Admin Password: ")
	while admin != adminpass:
		print "Incorrect Password!"
		admin = raw_input("Admin Password: ")
	print "Reboot COMPLETE!"
	print
	print "~~~~~ MINI COMPUTER V2.06 ~~~~~"
	print
	username = raw_input("Username: ")
	password = raw_input("Password: ")
	if username == user and password == pw:
		print "Logging in as",username+"..."
		print "Preparing Doors..."
		print "Welcome,",username+"..."
		print
		doors()
	else:
		print "Error invalid username or password!"
		print "Self-destruct initiated..."
		print "Self-destruct in T-..."
		time = 10
		while time != -1:
			print time
			time -= 1
		print "*BLACK SCREEN*"
		print "Contact a MINI COMPUTER 'EXPERT' to reboot your computer..."

def start():
	print "Starting MINI COMPUTER..."
	print
	print "~~~~~ MINI COMPUTER V2.06 ~~~~~"
	print
	username = raw_input("Username: ")
	password = raw_input("Password: ")

	if username == user and password == pw:
		print "Logging in as",username+"..."
		print "Preparing Doors..."
		print "Welcome,",username+"..."
		print
		doors()

	else:
		print "Error invalid username or password!"
		print "Self-destruct initiated..."
		print "Self-destruct in T-..."
		time = 10
		while time != -1:
			print time
			time -= 1
		print "*BLACK SCREEN*"
		print "Contact a MINI COMPUTER 'EXPERT' to reboot your computer..."
		reboot()

def doors():
	print "~~~~ Doors ~~~~"
	print
	print "Type (H)elp for help..."
	print
	while True:
		wat = raw_input("").lower()

		# [H]elp
		if wat == "h":
			print "Commands:"
			print "[H]elp.............Help"
			print "[T]ext.............Make a Text File"
			print "[O]pen [T]ext......Open a Text File"
			print "[S]how [T]exts.....Show all Text Files"
			print "[D]ate & [T]ime....Shows the current date and time"
			print "[C]amera...........Take a Picture/Selfie"
			print "[G]allery..........Take a look at your pictures"
			print "[R]estart..........Restart your Mini Computer"
			print "[L]og [O]ff........Log Off"

		# [T]ext
		elif wat == "t":
			title = raw_input("Title: ")
			text = raw_input("Text: ")
			texts[title] = text
			print "Text with the title,",title,", was created!"
		# [O]pen [T]ext
		elif wat == "ot":
			title = raw_input("What is the title of the text? ")
			print texts[title]
		# [S]how [T]exts
		elif wat == "st":
			print texts
		# [D]ate & [T]ime
		elif wat == "dt":
			print "%s/%s/%s" % (now.month, now.day, now.year)
			print "%s:%s" % (now.hour, now.minute)
		# [C]amera
		elif wat == "c":
			print "Type any letter/symbol/number then press ENTER to take a picture."
			lol = raw_input("")
			print "Photo saved! (Type [G] to view it)"
		# [G]allery
		elif wat == "g":
			print "---------------------------------------------------"
			print "|                    /VVVVVVVV\                   |"
			print "|                   |--_----_--|                  |"
			print "|                   |  O || O  |                  |"
			print "|                   |    88    |                  |"
			print "|                   \  \____/  /                  |"
			print "|                    \________/                   |"
			print "|                     |      |                    |"
			print "|                ____/        \____               |"
			print "|               /                  \              |"
			print "|              /                    \             |"
			print "---------------------------------------------------"
		# [R]estart
		elif wat == "r":
			print "RESTARTING..."
			print "RESTART COMPLETE"
		# [L]og [O]ut
		elif wat == "lo":
			start()
			break

		else:
			print "Invalid Command!!!"

start()
