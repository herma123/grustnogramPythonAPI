import requests, random, ast, json
from threading import Thread

class Client():



###										TOKEN



	def __init__(self, nickname = "", email = "", password = "", token = False):
		if 	 (nickname == "") and (email != "") and (password != "") and (token == False)	: 		self.token = self.login(email = email, password = password).json()["data"]["access_token"]
		elif (nickname != "") and (email != "") and (password != "") and (token == False)	: 		self.token = self.registration(nickname = nickname, email = email, password = password).json()["data"]["access_token"]
		elif (nickname == "") and (email == "") and (password == "") and (token != False)	: 	  	self.token = token



###										AUTHORIZATION



	def registration(self, nickname: str, email: str, password: str) -> bytes:

		return requests.post("https://api.grustnogram.ru/users", 
			data = {
				 "nickname"			: nickname,
				 "email"			: email,
				 "password"			: password,
				 "password_confirm" : password
			 })


	def login(self, email: str, password: str) -> bytes:

		return requests.post('https://api.grustnogram.ru/sessions?v=2', 
			data = {
				"email"	   : email,
				"password" : password
			})



###										MESSAGES



	def sendMessage(self, message = "", id_circle = 0, id_user = 0, reply_to = 0, my = 1, attachments = [], reactions = [], reply_msg = {}) -> bytes:

		return requests.post(f'https://msg.grustnogram.ru/circles/{id_circle}/messages', 
			headers = {"access-token": self.token}, 
			data = {
				"attachments" : attachments,
				"message"	  : message,
				"my"		  : my,
				"id"	  	  : id_circle, 
				"id_user"	  : id_user, 
				"reactions"	  : reactions,
				"reply_msg"	  : reply_msg,
				"reply_to"	  : reply_to
			})


	def deleteMessage(self, message_id = 0) -> bytes:

		return requests.delete(f"https://msg.grustnogram.ru/circles/message/{message_id}",
			headers = {"access-token": self.token})


	def getMessage(self, id_circle, limit = 1) -> dict:

		return requests.get(f"https://msg.grustnogram.ru/circles/{id_circle}/messages?id={id_circle}&limit={limit}",
			headers = {"access-token": self.token}).json()



###										USERS



	def getUser(self, nickname: str) -> dict:

		return requests.get(f"https://api.grustnogram.ru/users/{nickname}",
			headers = {"access-token": self.token}).json()


	def getSelf(self) -> dict:

		return requests.get(f"https://api.grustnogram.ru/users/self",
			headers = {"access-token": self.token}).json()


	def editSelf(self, name: str, nickname: str, about: str, url: str) -> bytes:

		return requests.put(f"https://api.grustnogram.ru/users/self",
			headers = {"access-token": self.token},
			data = {
				"name"		: name,
				"nickname"	: nickname,
				"about"		: about,
				"url"		: url
			})

	def editHand(self, hand_on = 1, hand_text = "example") -> bytes:

		return requests.put(f"https://api.grustnogram.ru/users/self",
			headers = {"access-token": self.token},
			data = {
				"hand_on"	: 1,
				"hand_text"	: hand_text
			})


	def follow(self, id_user = 0) -> bytes:

		return requests.post(f"https://api.grustnogram.ru/users/{id_user}/follow",
			headers = {"access-token": self.token})


	def unfollow(self, id_user = 0) -> bytes:

		return requests.delete(f"https://api.grustnogram.ru/users/{id_user}/follow",
			headers = {"access-token": self.token})


	def getFollowers(self, id_user = 0, limit = 1000) -> dict:

		return requests.get(f"https://api.grustnogram.ru/followers/{id_user}?limit={limit}&id={id_user}",
			headers = {"access-token": self.token}).json()

	def getFollow(self, id_user = 0, limit = 1000) -> dict:

		return requests.get(f"https://api.grustnogram.ru/follow/{id_user}?limit={limit}&id={id_user}",
			headers = {"access-token": self.token}).json()



###										CIRCLES



	def getCircleID(self, title: str) -> dict:
		return requests.get(f"https://api.grustnogram.ru/users/{title}",
			headers = {"access-token": self.token}).json()["data"]["id"]


	def getCircle(self, id_circle: int) -> dict:

		return requests.get(f"https://api.grustnogram.ru/circles/{id_circle}",
			headers = {"access-token": self.token}).json()


	def getCircles(self) -> dict:

		return requests.get(f"https://api.grustnogram.ru/circles",
			headers = {"access-token": self.token}).json()


	def getCirclesFromDialog(self, limit = 1000, type = 0) -> dict:

		return requests.get(f"https://msg.grustnogram.ru/dialogs?type={type}&limit={limit}",
			headers = {"access-token": self.token}).json()


	def getMembersCircle(self, id_circle = 0, limit = 1000, offset = 0) -> dict:
		return requests.get(f"https://api.grustnogram.ru/circles/{id_circle}/users?limit={limit}&offset={offset}",
			headers = {"access-token": self.token}).json()


	def enjoyCircle(self, id_circle) -> bytes:

		return requests.post(f"https://api.grustnogram.ru/circles/{id_circle}/enjoy", 
			headers = {"access-token": self.token},
			data = {
				"id"	: id_circle
			})


	def leftCircle(self, id_circle) -> bytes:

		return requests.post(f"https://api.grustnogram.ru/circles/{id_circle}/left", 
			headers = {"access-token": self.token},
			data = {
				"id"	: id_circle
			})


	def createCircle(self, title = "", avatar = "", desc = "", nickname = "", request_desc = "", anon = 0, hide = False, can_write = 1, privacy = 0, url = "", tags = [], moment = 0) -> bytes:
		
		return requests.post(f"https://api.grustnogram.ru/circles", 
			headers = {"access-token": self.token},
			data = {
				"title"			: title,
				"avatar"		: avatar,
				"desc"			: desc,
				"nickname"		: nickname,
				"request_desc"	: request_desc,
				"anon"			: anon,
				"hide"			: hide,
				"can_write"		: can_write,
				"privacy"		: privacy,
				"url"			: url,
				"tags"			: tags,
				"moment"		: moment
			})


	def editCircle(self, id_circle = 0, title = "", avatar = "", desc = "", nickname = "", request_desc = "", anon = 0, hide = False, can_write = 1, privacy = 0, url = "", tags = [], moment = 0) -> bytes:

		return requests.put(f"https://api.grustnogram.ru/circles/{id_circle}",
			headers = {"access-token": self.token},
			data = {
				"id"			: id_circle,
				"title"			: title,
				"avatar"		: avatar,
				"desc"			: desc,
				"nickname"		: nickname,
				"request_desc"	: request_desc,
				"anon"			: anon,
				"hide"			: hide,
				"can_write"		: can_write,
				"privacy"		: privacy,
				"url"			: url,
				"tags"			: tags,
				"moment"		: moment
			})


	def deleteMessagesFromCircle(self, id_circle) -> bytes:

		return requests.delete(f"https://api.grustnogram.ru/circles/{id_circle}/messages",
			headers = {"access-token": self.token})


	def deleteCircle(self, id_circle) -> bytes:

		return requests.delete(f"https://api.grustnogram.ru/circles/{id_circle}",
			headers = {"access-token": self.token})



###										POSTS



	def getPost(self, url: str) -> dict:

		return requests.get(f"https://api.grustnogram.ru/p/{url.split("https://grustnogram.ru/p/")[1]}?url={url.split("https://grustnogram.ru/p/")[1]}",
			headers = {"access-token": self.token}).json()


	def likePost(self, id_post) -> bytes:

		return requests.post(f"https://api.grustnogram.ru/posts/{id_post}/like",
			headers = {"access-token": self.token})


	def unlikePost(self, id_post) -> bytes:

		return requests.delete(f"https://api.grustnogram.ru/posts/{id_post}/like",
			headers = {"access-token": self.token})


	def commentPost(self, id_post, comment = "", reply_to = 0, privated = 0, attachments = []) -> bytes:

		return requests.post(f"https://api.grustnogram.ru/posts/{id_post}/comments",
			headers = {"access-token": self.token},
			data = {
				"comment"		: comment,
				"reply_to"		: reply_to,
				"privated"		: privated,
				"attachments"	: attachments
			})


	def deleteCommentPost(self, id_comment) -> bytes:

		return requests.delete(f"https://api.grustnogram.ru/posts/comments/{id_comment}",
			headers = {"access-token": self.token})
