from client import Client

client = Client(email = "example@gmail.com", password = "password")
user_poem = client.getUser("nicknameUser")["data"]["poem"]



print(f'{user_poem["title"]} | {user_poem["author"]}\n\n{user_poem["poem"]}')
