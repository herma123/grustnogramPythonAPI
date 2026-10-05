from client import Client

client = Client(email = "example@mail.com", password = "password")
user_poem = client.getUser("username")["data"]["poem"]



print(f'{user_poem["title"]} | {user_poem["author"]}\n\n{user_poem["poem"]}')
