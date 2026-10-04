from client import Client


client = Client(email = "example@mail.com", password = "password")
last_messages = []


while True:

	for x in client.getCirclesFromDialog()["data"]:

		last_message = x["last_message"]
		message_list = last_message["message"].split()

		if last_message["id"] not in last_messages:

			if "/start" == message_list[0]:
				client.sendMessage(message = "Hello, World!", id_circle = x["id"], reply_to = last_message["id"])
				last_messages.append(last_message["id"])
