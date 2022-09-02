import os # OS related - find file
import pickle

# Book Class ( Parent / Super / Base Class)
class Book():
    def __init__(self, name, isbn):
        self.__name = name
        self.__isbn = isbn
        self.__list = []

    # Get/Set Function (Member functions)
    # Book Name
    def getName(self):
        return self.__name

    def setName(self, new_name):
        self.__name = new_name

    # ISBN
    def getISBN(self):
        return self.__isbn

    def setISBN(self, new_isbn):
        self.__isbn = new_isbn

    def readFile(self, filename):
        if (os.path.exists(filename)):
            file = open(filename, 'rb') # read as binary file
            if (file):
                # read all contents from file and save into data
                data = pickle.load(file)
                self.__name = data.getName()
                self.__isbn = data.getISBN()
                file.close()

    def writeFile(self, filename):
        file = open(filename, 'wb') # write as binary file
        if (file):
            pickle.dump(self, file)
            file.close()

