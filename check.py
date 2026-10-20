from datetime import datetime
import requests

count  = 0

with open("sites.txt") as file:
	for line in file:
		now =  datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		count = count + 1
		url = line.strip()
		try:
			response =  requests.get(url, timeout=5)
			if  response.status_code == 200:
				print(now ,"UP", url)
			else:
				print(now,"DOWN",url,response.status_code)
		except requests.exceptions.RequestException:
			print(now, "DOWN", url, "no answer")
	print("Checked", count, "sites")
