from client import Client

client = Client(email = "example@mail.com", password = "password")
id_user = client.getUser("username")["data"]["id"]



client.follow(id_user = id_user)
