from client import Client

#login
client = Client(email = "example@mail.com", password = "example")

#get Token

print(client.token)

#send message
user.sendMessage(message = "example", id_circle = 01234567)

#delete message
user.deleteMessage(message_id = 01234567)

#get message
user.getMessage(id_circle = 01234567)

#get user
user.getUser(nickname = "example")

#get circle
user.getCircle(id_circle = 01234567)