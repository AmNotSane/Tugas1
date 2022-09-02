from book import Book
import os
import pickle

adminUsername = 'Darrick'
adminpassword = 'HelloWorld'


class Account():
	def __init__(self, username, password):
		self.username = username
		self.password = password

	def loadAccount(self, filename):
		if (os.path.exists(filename)):
			file = open(filename, 'rb')
			if (file):
				pickle.load(file)
	
	def Login(self, username, password):
		return f'Hello {username} you have logged in successfully!'
				



	def write_File(self, filename):
		file = open(filename, 'wb')
		if (file):
			pickle.dump(username, password, file)
			file.close() 
			
		else:
			username = input('Please enter a username: ')
			password = input('Please enter a password: ')
			return (username, password)
			

class Book():
	def __init__(self,book, isbn):
		self.book = book
		self.isbn = isbn

	def book_status(self, book):
		if book in book_name:
			book_status = 'available'
		else:
			book_status = 'unavailable'
		return book_status

	def isbn_status(self, isbn):
		if isbn in isbnAvailability:
			isbn_status = 'available'
		else:
			isbn_status = 'unavailable'
		return isbn_status

class Transaction():


	def 




