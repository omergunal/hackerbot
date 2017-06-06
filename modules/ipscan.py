import json
import urllib
from virustotal_api import api

def Ipscan1(message):
	if api == "XXX":
		print("\033[93m {}\033[00m" .format("*****************************************************"))
		print("\033[93m {}\033[00m" .format("Please fill in the virustotal_api.py for access virustotal api"))
		print("\033[93m {}\033[00m" .format("*****************************************************"))

	else:
		try:

			url = 'https://www.virustotal.com/vtapi/v2/ip-address/report'

			parameters = {'ip': message, 'apikey': api}

			response = urllib.urlopen('%s?%s' % (url, urllib.urlencode(parameters))).read()
			response_dict = json.loads(response)
			resolutions = response_dict.get("resolutions")

			for x in resolutions:
				print(str(x.get("last_resolved")) +"  " +str(x.get("hostname")) )

		except:
			print("Somethings wrong...")

