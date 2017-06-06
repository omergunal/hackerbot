import requests
from virustotal_api import api

def Urlscan1(message):
	if api == "XXX":
		print("\033[93m {}\033[00m" .format("*****************************************************"))
		print("\033[93m {}\033[00m" .format("Please fill in the virustotal_api.py for access virustotal api"))
		print("\033[93m {}\033[00m" .format("*****************************************************"))

	else:
		try:

			headers = {
			  "Accept-Encoding": "gzip, deflate",
			  "User-Agent" : "gzip,  My Python requests library example client or username"
			  }
			params = {'apikey': api, 'resource': message} # message is target url
			response = requests.post('https://www.virustotal.com/vtapi/v2/url/report',
			  params=params, headers=headers)
			json_response = response.json()

			positives = json_response.get("positives") #detection
			total = json_response.get("total") # total scan
			scan = json_response.get("scans") # scan data


			print("\033[93m {}\033[00m" .format("*****************************************************"))

			for firms in scan: #List what they detected
				a = scan.get(firms)
				detected = str(a.get("detected"))
				if detected == "True":
					print("\033[92m {}\033[00m" .format(str(firms)) + " : " + str(a.get("result")) )



			print("\033[91m {}\033[00m" .format("Detection ratio: " + str(positives) + "/" + str(total))) # detection ratio

			print("\033[93m {}\033[00m" .format("*****************************************************"))

		except:
			print("Somethings wrong...")

