from client import Client

client = Client(email = "example@mail.com", password = "password")

client.sendMessage(message = "Hello, World!", id_circle = 01234567)