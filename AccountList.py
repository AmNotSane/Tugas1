import os
import pickle

adminUsername = 'Darrick'
adminpassword = 'HelloWorld'


class AccountList():
	def __init__(self, filename, username, password):
		self.filename = filename
		self.username = username
		self.password = password
		self.__list = []

	def loadAccount(self):
		if (os.path.exists(self.filename)):
			file = open(self.filename, 'rb')
			if (file):
				self.__list = pickle.load(file)
				file.close()

	def write_File(self):
		file = open(self.filename, 'wb')
		if (file):
			pickle.dump(self.__list, file)
			file.close() 
	
	def getUser(self):
		return self.username

	def ifExist(self):
		if (self.username or self.password):
			return True
		else:
			False
	
	def addAccount(self):
		user = self.__list.append(self.username)
		passw = self.__list.append(self.password)
		return user and passw

	def delete_Account(self):
		if self.username in self.__list:
			return self.__list.pop(self.username)
		else:
			pass
		
	def getList(self):
		return self.__list

	def editAccount(self, password):
		if self.username in self.__list:
			for x in range(len(self.__list)):
				if x == self.__list.index(self.password):
					self.__list[x] = password
					return self.__list
		else:
			pass
		

account1 = AccountList('test', 'name', 'word')
account1.addAccount()
print(account1. getList())
account1.editAccount('drow')
print(account1. getList())
