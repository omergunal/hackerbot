import os
import sys
sys.path.append("modules/")
import helper
import filescan
import urlscan
import ipscan

def Commands(message):

	try:
		if message[0] == "!help":
			helper.Features() # Write all features of the bot
		elif message[0] == "!twitter":
			if message[1][:1] == "@":
				try:
					os.system("python3 modules/tweets_analyzer.py -n " + message[1][1:]) # run tweets analyzer
				except:
					print("There is a problem.Did you write username? Please try again. !twitter @username")
			else:
				print("Bad syntax,dont forget use '@' .Try again, !twitter @username")	
		elif message[0] == "!filescan":
			if message[1]:
				try:	
					filescan.Filescan1(message[1])
				except:
					print("Check file path please")
			else:
				print("Bad syntax")	

		elif message[0] == "!urlscan":
			if message[1]:
				try:
					urlscan.Urlscan1(message[1])
				except:
					print("Check url please")
			else:
				print("Bad syntax")

		elif message[0] == "!ipscan":
			if message[1]:
				try:
					ipscan.Ipscan1(message[1])
				except:
					print("Check IP please")


		elif message[0] == "!linuxenum":
			try:
				os.system("./modules/linuxenum.sh")
			except:
				print("Hmm,there is a problem")


		elif message[0] == "!linuxprivchecker":
			try:
				os.system("python modules/linuxprivchecker.py")
			except:
				print("There is a problem with this tool")

		elif message[0] == "!shellshock":
			try:
				os.system("./modules/shellshock.sh")
			except:
				print("There is a problem with this tool")

		elif message[0] == "!mimipenguin":
			try:
				os.system("./modules/mimipenguin.sh")
			except:
				print("There is a problem with this tool")

		else:
			print("I dont know this command")

	except:
		print("**Try again, check your syntax. You can use !help command")
