from client import Client

client = Client(email = "genocidePalestine", password = "1y2e7i9s")
user_poem = client.getUser("genocidepalestine")["data"]["poem"]



print(f'{user_poem["title"]} | {user_poem["author"]}\n\n{user_poem["poem"]}')