from client import Client

client = Client(email = "example@mail.com", password = "password")
id_user = client.getUser("username")["data"]["id"]



while True:
	client.follow(id_user = id_user)
	client.unfollow(id_user = id_user)