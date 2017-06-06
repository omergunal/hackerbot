def Features():
	start = "\033[1m"
	end = "\033[0;0m"

	print(start+"\033[93m {}\033[00m" .format("Twitter account analysis -->")+end+" !twitter @username")
	print(start+"\033[93m {}\033[00m" .format("URL scan -->")+end+" !urlscan http://website.com")
	print(start+"\033[93m {}\033[00m" .format("File scan -->")+end+" !filescan /file_path/ --> !filescan /home/chatbot/malware.exe")	
	print(start+"\033[93m {}\033[00m" .format("IP scan -->")+end+" !ipscan IP_ADDRESS")
	print(start+"\033[93m {}\033[00m" .format("Linux enumeration  -->")+end+" !linuxenum")
	print(start+"\033[93m {}\033[00m" .format("Linux privilege escalation checker -->")+end+" !linuxprivchecker")
	print(start+"\033[93m {}\033[00m" .format("Shellshock -->")+end+" !shellshock")
	print(start+"\033[93m {}\033[00m" .format("Mimipenguin (A tool to dump the login password from the current linux desktop user)-->")+end+" !mimipenguin")


