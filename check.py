from datetime import datetime
now =  datetime.now().strftime("%Y-%m-%d %H:%M:%S")

count  = 0

with open("sites.txt") as file:
	for line in file:
		url = line.strip()
		print(now, "Checking", url)
		count = count + 1
	print("Checked", count, "sites")

