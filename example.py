from client import Client

#login
client = Client(email = "example@mail.com", password = "example")

#get Token

print(client.token)

#send message
client.sendMessage(message = "example", id_circle = 01234567)

#delete message
client.deleteMessage(message_id = 01234567)

#get message
client.getMessage(id_circle = 01234567)

#get user
client.getUser(nickname = "example")

#get circle
client.getCircle(id_circle = 01234567)
