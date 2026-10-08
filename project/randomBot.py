from client import Client
import random


client = Client(email = "example@mail.com", password = "password")
last_messages = []


while True:

	for x in client.getCirclesFromDialog()["data"]:

		last_message = x["last_message"]
		message_list = last_message["message"].split()

		if last_message["id"] not in last_messages:

			if "/start" == message_list[0]:
				client.sendMessage(message = """This is a bot that selects numbers from a random range.
To use it, enter /r [lower number of the range] [upper number of the range]
 Example: /r 1 100""", id_circle = x["id"], reply_to = last_message["id"])
				last_messages.append(last_message["id"])


			elif "/r" == message_list[0]:
				client.sendMessage(message = random.randint(int(message_list[1]), int(message_list[2])), id_circle = x["id"], reply_to = last_message["id"])


