class User:
    def __init__(self, userName=None):
        self.userName = userName

class Friend:
    def __init__(self, friendName=None):
        self.friendName = friendName

class Movie:
    def __init__(self, id=0, title=None, year=0, minutes=0, genre=None, format=None):
        self.id = id
        self.title = title
        self.year = year
        self.minutes = minutes
        self.genre = genre
        self.format = format

class TV:
    def __init__(self, id=0, title=None, year=0, genre=None):
        self.id = id
        self.title = title
        self.year = year
        self.genre = genre

class Book:
    def __init__(self, id=0, title="", year=0, authors=None, genre=None, format=None):
        self.id = id
        self.title = title
        self.year = year
        self.authors = authors
        self.genre = genre
        self.format = format

    def __str__(self):
        return self.title + "by " + str(self.authors)

    def getDescription(self):
        return self.title + " by " + self.authors
                
class Author:
    def __init__(self, firstName="", lastName=""):
        self.firstName = firstName
        self.lastName = lastName

    def __str__(self):
        return self.firstName + " " + self.lastName

class Authors:
    def __init__(self):
        self.__list = []

    def add(self, author):
        self.__list.append(author)

    @property
    def count(self):
        return len(self.__list)

    def __str__(self):
        author_string = ""
        for author in self.__list:
            author_string += str(author) + ", "
        author_string = author_string[:-2] #Strips last comma... huh.
        return author_string

    def __iter__(self):
        self.__index = -1
        return self

    def __next__(self):
        if self.__index == len(self.__list)-1:
            raise StopIteration         
        self.__index += 1
        author = self.__list[self.__index]
        return author

class Genre:
    def __init__(self, id=0, name=None):
        self.id = id
        self.name = name

class Format:
    def __init__(self, id=0, name=None, type=None):
        self.id = id
        self.name = name
        self.type = type