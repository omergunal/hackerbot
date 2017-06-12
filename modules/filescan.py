import requests
from virustotal_api import api


def Filescan1(message, banner="*" * 53, request_url="https://www.virustotal.com/vtapi/v2/file"):
	
	if api == "XXX":		
		print("\033[93m {}\033[00m".format(banner))
		print("\033[93m Please fill in the virustotal_api.py for access to the API..\033[00m")
		print("\033[93m {}\033[00m".format(banner))

	else:
		try:
			params = {'apikey': api}
			files = {'file': ('files', open(message, 'rb'))} # file name
			response = requests.post(request_url + "/scan", files=files, params=params)
			json_response = response.json()
			resource = json_response.get("resource") # resource 
			print(resource)

			params = {'apikey': api, 'resource': resource}
			headers = {
			  "Accept-Encoding": "gzip, deflate",
			  "User-Agent" : "gzip,  My Python requests library example client or username"
			  }
			response = requests.get(request_url + "/report",
			  params=params, headers=headers)
			file_response = response.json()

			positives = file_response.get("positives") # detection number 
			total = file_response.get("total") # total scan
			scan = file_response.get("scans") # scan data
			print("\033[93m {}\033[00m".format(banner))
			for firms in scan: #List what they detected
				a = scan.get(firms)
				detected = str(a.get("detected"))
				if detected == "True": 
					print("\033[92m {}:{}\033[00m".format(str(firms), str(a.get("result"))))
					
			print("\033[91m {}\033[00m".format("Detection ratio: {}/{}".format(str(positives), str(total))))
			print("\033[93m {}\033[00m".format(banner))

		except Exception:
			print("Something went wrong... Please check your file path...")
