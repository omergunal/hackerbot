import json
import urllib
from virustotal_api import api

def Ipscan1(message, banner="*" * 53, url='https://www.virustotal.com/vtapi/v2/ip-address/report'):
	if api == "XXX":
		print("\033[93m {}\033[00m".format(banner))
		print("\033[93m Please fill in the virustotal_api.py for access virustotal api\033[00m")
		print("\033[93m {}\033[00m".format(banner))

	else:
		try:
			parameters = {'ip': message, 'apikey': api}

			response = urllib.urlopen('%s?%s' % (url, urllib.urlencode(parameters))).read()
			response_dict = json.loads(response)
			resolutions = response_dict.get("resolutions")

			for x in resolutions:
				print(str(x.get("last_resolved")) +"  " +str(x.get("hostname")) )

		except Exception:
			print("Somethings wrong...")

