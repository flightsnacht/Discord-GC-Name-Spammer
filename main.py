import requests, time, json, sys

with open("settings.json", "r") as f:
	data = json.load(f)
token = data["token"]
channelid = data["channelid"]

groupchatname = input("What would you like the group chat name to be?: ")
input("Press 'ENTER' to start spamming.")
print("Press 'CTRL + C' to stop spamming.")
num = 0
try:
	while True:
		num = num + 1
		payload = {
			'name': f"{num} || {groupchatname}"
		}
		headers = {
			'authorization': token
		}
		r = requests.patch("https://discord.com/api/v9/channels/" + channelid, json=payload, headers=headers)
		if r.status_code == 200:
			print(f"Channel name changed to {groupchatname} || {num}")
		elif r.status_code == 429:
			j = r.json()
			ratelimit_length = float(j['retry_after'])
			print(f"Ratelimited, sleeping for {ratelimit_length} seconds.")
			time.sleep(ratelimit_length)
			r = requests.patch("https://discord.com/api/v9/channels/" + channelid, json=payload, headers=headers)
			print(f"Channel name changed to {groupchatname} || {num}")
		else:
			input("Error, please check your token and channel ID")
			sys.exit()
except KeyboardInterrupt:
	input("Spamming stopped, press 'ENTER' to quit")
	sys.exit()