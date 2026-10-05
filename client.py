import requests, json

class Client():



###										TOKEN



	def __init__(self, nickname = "", email = "", password = "", token = False, proxies = {}):
		if 	 (nickname == "") and (email != "") and (password != "") and (token == False)	: 		self.token = self.login(email = email, password = password, proxies = proxies)["data"]["access_token"]; self.email = email; self.password = password
		elif (nickname != "") and (email != "") and (password != "") and (token == False)	: 		self.token = self.registration(nickname = nickname, email = email, password = password, proxies = proxies)["data"]["access_token"]; self.nickname = nickname; self.password = password
		elif (nickname == "") and (email == "") and (password == "") and (token != False)	: 	  	self.token = token



###										AUTHORIZATION



	def registration(self, nickname, email, password, proxies = {}) -> dict:

		return requests.post("https://api.grustnogram.ru/users", 
			data = {
				 "nickname"			: nickname,
				 "email"			: email,
				 "password"			: password,
				 "password_confirm" : password
			},
			proxies = proxies).json()


	def login(self, email, password, proxies = {}) -> dict:

		return requests.post('https://api.grustnogram.ru/sessions?v=2', 
			data = {
				"email"	   : email,
				"password" : password
			},
			proxies = proxies).json()



###										MESSAGES



	def sendMessage(self, message = "", id_circle = 0, id_user = 0, reply_to = 0, my = 1, attachments = [], reactions = [], reply_msg = {}, proxies = {}) -> dict:

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
			},
			proxies = proxies).json()


	def deleteMessage(self, message_id = 0, proxies = {}) -> dict:

		return requests.delete(f"https://msg.grustnogram.ru/circles/message/{message_id}",
			headers = {"access-token": self.token},
			proxies = proxies).json()


	def getMessage(self, id_circle, limit = 1, proxies = {}) -> dict:

		return requests.get(f"https://msg.grustnogram.ru/circles/{id_circle}/messages?id={id_circle}&limit={limit}",
			headers = {"access-token": self.token},
			proxies = proxies).json()



###										USERS



	def getUser(self, nickname, proxies = {}) -> dict:

		return requests.get(f"https://api.grustnogram.ru/users/{nickname}",
			headers = {"access-token": self.token},
			proxies = proxies).json()


	def getSelf(self, proxies = {}) -> dict:

		return requests.get(f"https://api.grustnogram.ru/users/self",
			headers = {"access-token": self.token},
			proxies = proxies).json()


	def editSelf(self, name, nickname, about, url, proxies = {}) -> dict:

		return requests.put(f"https://api.grustnogram.ru/users/self",
			headers = {"access-token": self.token},
			data = {
				"name"		: name,
				"nickname"	: nickname,
				"about"		: about,
				"url"		: url
			},
			proxies = proxies).json()

	def editHand(self, hand_on = 1, hand_text = "example", proxies = {}) -> dict:

		return requests.put(f"https://api.grustnogram.ru/users/self",
			headers = {"access-token": self.token},
			data = {
				"hand_on"	: 1,
				"hand_text"	: hand_text
			},
			proxies = proxies).json()


	def follow(self, id_user = 0, proxies = {}) -> dict:

		return requests.post(f"https://api.grustnogram.ru/users/{id_user}/follow",
			headers = {"access-token": self.token},
			proxies = proxies).json()


	def unfollow(self, id_user = 0, proxies = {}) -> dict:

		return requests.delete(f"https://api.grustnogram.ru/users/{id_user}/follow",
			headers = {"access-token": self.token},
			proxies = proxies).json()


	def getFollowers(self, id_user = 0, limit = 1000, proxies = {}) -> dict:

		return requests.get(f"https://api.grustnogram.ru/followers/{id_user}?limit={limit}&id={id_user}",
			headers = {"access-token": self.token},
			proxies = proxies).json()

	def getFollow(self, id_user = 0, limit = 1000, proxies = {}) -> dict:

		return requests.get(f"https://api.grustnogram.ru/follow/{id_user}?limit={limit}&id={id_user}",
			headers = {"access-token": self.token},
			proxies = proxies).json()



###										CIRCLES



	def getCircleID(self, title, proxies = {}) -> int:
		return requests.get(f"https://api.grustnogram.ru/users/{title}",
			headers = {"access-token": self.token},
			proxies = proxies).json()["data"]["id"]


	def getCircle(self, id_circle, proxies = {}) -> dict:

		return requests.get(f"https://api.grustnogram.ru/circles/{id_circle}",
			headers = {"access-token": self.token},
			proxies = proxies).json()


	def getCircles(self, proxies = {}) -> dict:

		return requests.get(f"https://api.grustnogram.ru/circles",
			headers = {"access-token": self.token},
			proxies = proxies).json()


	def getCirclesFromDialog(self, limit = 1000, type = 0, proxies = {}) -> dict:

		return requests.get(f"https://msg.grustnogram.ru/dialogs?type={type}&limit={limit}",
			headers = {"access-token": self.token},
			proxies = proxies).json()


	def getMembersCircle(self, id_circle = 0, limit = 500, proxies = {}) -> dict:
		return requests.get(f"https://api.grustnogram.ru/circles/{id_circle}/users?limit={limit}",
			headers = {"access-token": self.token},
			proxies = proxies).json()


	def enjoyCircle(self, id_circle, proxies = {}) -> dict:

		return requests.post(f"https://api.grustnogram.ru/circles/{id_circle}/enjoy", 
			headers = {"access-token": self.token},
			data = {
				"id"	: id_circle
			},
			proxies = proxies).json()


	def leftCircle(self, id_circle, proxies = {}) -> dict:

		return requests.post(f"https://api.grustnogram.ru/circles/{id_circle}/left", 
			headers = {"access-token": self.token},
			data = {
				"id"	: id_circle
			},
			proxies = proxies).json()


	def createCircle(self, title = "", avatar = "", desc = "", nickname = "", request_desc = "", anon = 0, hide = False, can_write = 1, privacy = 0, url = "", tags = [], moment = 0, proxies = {}) -> dict:
		
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
			},
			proxies = proxies).json()


	def editCircle(self, id_circle = 0, title = "", avatar = "", desc = "", nickname = "", request_desc = "", anon = 0, hide = False, can_write = 1, privacy = 0, url = "", tags = [], moment = 0, proxies = {}) -> dict:

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
			},
			proxies = proxies).json()


	def deleteMessagesFromCircle(self, id_circle, proxies = {}) -> dict:

		return requests.delete(f"https://api.grustnogram.ru/circles/{id_circle}/messages",
			headers = {"access-token": self.token},
			proxies = proxies).json()


	def deleteCircle(self, id_circle, proxies = {}) -> dict:

		return requests.delete(f"https://api.grustnogram.ru/circles/{id_circle}",
			headers = {"access-token": self.token},
			proxies = proxies).json()



###										POSTS



	def getPost(self, url, proxies = {}) -> dict:

		return requests.get(f"https://api.grustnogram.ru/p/{url.split("https://grustnogram.ru/p/")[1]}?url={url.split("https://grustnogram.ru/p/")[1]}",
			headers = {"access-token": self.token},
			proxies = proxies).json()


	def getPosts(self, limit = 10, type = "new", type_count = "1", proxies = {}) -> dict:

		return requests.get(f"https://api.grustnogram.ru/posts?{type}={type_count}&limit={limit}",
			headers = {"access-token": self.token},
			proxies = proxies).json()


	def loadPost(self, _filter = 0, text = "", media = [""], id_circle = 0, circle_only = 0) -> dict:

		return requests.post("https://api.grustnogram.ru/posts",
			headers = {"access-token": self.token},
			data={
			"filter"		: _filter,
			"text"			: text,
			"media"			: media, 
			"id_circle"		: id_circle,
			"circle_only"	: circle_only},
			proxies = proxies).json()


	def deletePost(self, id_post = 0):
		return requests.delete(f"https://api.grustnogram.ru/posts/{id_post}",
			headers = {"access-token": self.token},
			proxies = proxies).json()


	def likePost(self, id_post, proxies = {}) -> dict:

		return requests.post(f"https://api.grustnogram.ru/posts/{id_post}/like",
			headers = {"access-token": self.token},
			proxies = proxies).json()


	def unlikePost(self, id_post, proxies = {}) -> dict:

		return requests.delete(f"https://api.grustnogram.ru/posts/{id_post}/like",
			headers = {"access-token": self.token},
			proxies = proxies).json()


	def repostPost(self, id_post, proxies = {}) -> dict:
		return requests.post(f"https://api.grustnogram.ru/posts/{id_post}/repost",
			headers = {"access-token": self.token},
			proxies = proxies).json()


	def favoritePost(self, id_post, proxies = {}) -> dict:

		return requests.post(f"https://api.grustnogram.ru/posts/{id_post}/favorite",
			headers = {"access-token": self.token},
			proxies = proxies).json()


	def unfavoritePost(self, id_post, proxies = {}) -> dict:

		return requests.delete(f"https://api.grustnogram.ru/posts/{id_post}/favorite",
			headers = {"access-token": self.token},
			proxies = proxies).json()


	def likeCommentPost(self, id_comment, proxies = {}) -> dict:

		return requests.post(f"https://api.grustnogram.ru/comments/{id_comment}/like",
			headers = {"access-token": self.token},
			proxies = proxies).json()


	def unlikeCommentPost(self, id_comment, proxies = {}) -> dict:

		return requests.delete(f"https://api.grustnogram.ru/comments/{id_comment}/like",
			headers = {"access-token": self.token},
			proxies = proxies).json()


	def commentPost(self, id_post, comment = "", reply_to = 0, privated = 0, attachments = [], proxies = {}) -> dict:

		return requests.post(f"https://api.grustnogram.ru/posts/{id_post}/comments",
			headers = {"access-token": self.token},
			data = {
				"comment"		: comment,
				"reply_to"		: reply_to,
				"privated"		: privated,
				"attachments"	: attachments
			},
			proxies = proxies).json()


	def deleteCommentPost(self, id_comment, proxies = {}) -> dict:

		return requests.delete(f"https://api.grustnogram.ru/posts/comments/{id_comment}",
			headers = {"access-token": self.token},
			proxies = proxies).json()
