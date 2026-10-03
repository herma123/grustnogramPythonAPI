import requests, random, ast, json
from threading import Thread

class Client():

	def __init__(self, nickname = "", email = "", password = "", token = False):
		if 	 (nickname == "") and (email != "") and (password != "") and (token == False)	: 		self.token = self.login(email = email, password = password).json()["data"]["access_token"]
		elif (nickname != "") and (email != "") and (password != "") and (token == False)	: 		self.token = self.registration(nickname = nickname, email = email, password = password).json()["data"]["access_token"]
		elif (nickname == "") and (email == "") and (password == "") and (token != False)	: 	  	self.token = token


	def registration(self, nickname: str, email: str, password: str):

		return requests.post("https://api.grustnogram.ru/users", 
			data = {
			 "nickname"			: nickname,
			 "email"			: email,
			 "password"			: password,
			 "password_confirm" : password
			 })


	def login(self, email: str, password: str):

		return requests.post('https://api.grustnogram.ru/sessions?v=2', 
			data = {
			"email"	   : email,
			"password" : password
			})


	def sendMessage(self, message = "", id_circle = 0, id_user = 0, reply_to = 0, my = 1, attachments = [], reactions = [], reply_msg = {}):

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


	def deleteMessage(self, message_id = 0):

		return requests.delete(f"https://msg.grustnogram.ru/circles/message/{message_id}",
			headers = {"access-token": self.token})


	def getMessage(self, id_circle, limit = 1):

		return requests.get(f"https://msg.grustnogram.ru/circles/{id_circle}/messages?id={id_circle}&limit={limit}", headers = {"access-token": self.token}).json()


	def getUser(self, nickname: str):

		return requests.get(f"https://api.grustnogram.ru/users/{nickname}").json()


	def getCircle(self, id_circle: int):

		return requests.get(f"https://api.grustnogram.ru/circles/{id_circle}",
			headers = {"access-token": self.token}).json()