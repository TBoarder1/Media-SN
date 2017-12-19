#!/usr/bin/env/python3

import db
from objects import Book
from objects import Movie

#MENU FUNCTIONS

def display_main_menu():
    print("MAIN MENU")
    print("1  - Movies program")
    print("2  - Books program")
    #print("3  - TV program")
    print("0  - Exit program")
    print()

def display_book_title():
    print("The Book List program")
    print()    
    display_book_menu()

def display_movie_title():
    print("The Movie List program")
    print()    
    display_movie_menu()

def display_tv_title():
    print("The TV List program")
    print()    
    display_tv_menu()

def display_book_menu():
    print("BOOK COMMAND MENU")
    print("1  - View all books")
    print("2  - View books by genre")
    print("3  - View books by format")
    print("4  - View books by year")
    print("5  - Add a book")
    print("6  - Delete a book")
    print("7  - View shared books")
    print("0  - Returns to Previous Menu")
    print()

def display_movie_menu():
    print("MOVIE COMMAND MENU")
    print("1  - View all movies")
    print("2  - View movies by genre")
    print("3  - View movies by format")
    print("4  - View movies by year")
    print("5  - View movies with runtime under given length")
    print("6  - Add a movie")
    print("7  - Delete a movie")
    print("8  - View Shared Movies")
    print("0  - Returns to Previous Menu")
    print()

def display_tv_menu():
    print("TV COMMAND MENU")
    print("1  - View movies by category")
    print("2  - View movies by year") 
    print("3  - View movies with runtime under given length")
    print("4  - Add a movie")
    print("5  - Delete a movie")
    print("0  - Returns to Previous Menu")
    print()

def book_menu():
    display_book_title()
    display_book_formats()
    display_genres()
    while True:        
        command = input("Command: ")
        if command == "1":
            display_all_books()
        elif command == "2":
            display_books_by_genre()
        elif command == "3":
            display_books_by_format()
        elif command == "4":
            display_books_by_year()
        elif command == "5":
            add_book()
        elif command == "6":
            delete_book()
        elif command == "7":
            view_shared_books()
        elif command == "0":
            display_main_menu()
            break
        else:
            print("Not a valid command. Please try again.\n")
            display_book_menu()
    
def movie_menu():
    display_movie_title()
    display_movie_formats()
    display_genres()
    while True:        
        command = input("Command: ")
        if command == "1":
            display_all_movies()
        elif command == "2":
            display_movies_by_genre()
        elif command == "3":
            display_movies_by_format()
        elif command == "4":
            display_movies_by_year()
        elif command == "5":
            display_movies_by_minutes()
        elif command == "6":
            add_movie()
        elif command == "7":
            delete_movie()
        elif command == "8":
            view_shared_movies()            
        elif command == "0":
            display_main_menu()
            break
        else:
            print("Not a valid command. Please try again.\n")
            display_movie_menu()

def tv_menu():
    display_movie_title()
    display_formats()
    display_genres()
    while True:        
        command = input("Command: ")
        if command == "1":
            display_movies_by_genre()
        elif command == "2":
            display_movies_by_year()
        elif command == "3":
            display_movies_by_minutes()
        elif command == "4":
            add_movie()
        elif command == "5":
            delete_movie()
        elif command == "0":
            break
        else:
            print("Not a valid command. Please try again.\n")
            display_tv_menu()

#DISPLAY OBJECTS
    
def display_genres():
    print("GENRES")
    genres = db.get_genres()    
    for genre in genres:
        print(str(genre.id) + ". " + genre.name)
    print()

def display_book_formats():
    print("FORMATS")
    formats = db.get_formats()    
    for format in formats:
        if str(format.type) == "book":
            print(str(format.id) + ". " + format.name + ". " + (str(format.type)))
    print()

def display_movie_formats():
    print("FORMATS")
    formats = db.get_formats()    
    for format in formats:
        if str(format.type) == "video":
            print(str(format.id) + ". " + format.name + ". " + (str(format.type)))
    print()

def display_books(books, title_term):
    print("BOOKS - " + title_term)
    line_format = "{:3s} {:37s} {:6s} {:37s} {:10s} {:14s}"
    print(line_format.format("ID", "Title", "Year", "Authors", "Genre", "Format"))
    print("-" * 107)
    for book in books:
        print(line_format.format(str(book.id), book.title,
                                 str(book.year), str(book.authors),
                                 book.genre.name, book.format.name))
    print()

def display_movies(movies, title_term):
    print("MOVIES - " + title_term)
    line_format = "{:3s} {:37s} {:6s} {:5s} {:10s} {:10s}"
    print(line_format.format("ID", "Title", "Year", "Mins", "Category", "Format"))
    print("-" * 74)
    for movie in movies:
        print(line_format.format(str(movie.id), movie.title,
                                 str(movie.year), str(movie.minutes),
                                 movie.genre.name, movie.format.name))
    print()
    
def display_tv(tv, title_term):
    print("TV - " + title_term)
    line_format = "{:3s} {:37s} {:6s} {:5s} {:10s}"
    print(line_format.format("ID", "Title", "Year", "Mins", "Category"))
    print("-" * 64)
    for tv in tvs:
        print(line_format.format(str(tv.id), tv.title,
                                 str(tv.year), str(tv.minutes),
                                 tv.genre.name))
    print()

#DISPLAY ALL

def display_all_books():
    print()
    books = db.get_all_books()
    display_books(books, "ALL")

def display_all_movies():
    print()
    movies = db.get_all_movies()
    display_movies(movies, "ALL")

#DISPLAY BY GENRE

def display_books_by_genre():
    genre_id = int(input("Genre ID: "))
    genre = db.get_genre(genre_id)
    if genre == None:
        print("There is no genre with that ID.\n")
    else:
        print()
        books = db.get_books_by_genre(genre_id)
        display_books(books, genre.name.upper())

def display_movies_by_genre():
    genre_id = int(input("Genre ID: "))
    genre = db.get_genre(genre_id)
    if genre == None:
        print("There is no genre with that ID.\n")
    else:
        print()
        movies = db.get_movies_by_genre(genre_id)
        display_movies(movies, genre.name.upper())

def display_tv_by_genre():
    genre_id = int(input("Genre ID: "))
    genre = db.get_genre(genre_id)
    if genre == None:
        print("There is no genre with that ID.\n")
    else:
        print()
        tv = db.get_tv_by_genre(genre_id)
        display_tv(tv, genre.name.upper())

#DISPLAY BY FORMAT

def display_books_by_format():
    format_id = int(input("Format ID: "))
    format = db.get_format(format_id)
    if format == None:
        print("There is no format with that ID.\n")
    else:
        print()
        books = db.get_books_by_format(format_id)
        display_books(books, format.name.upper())

def display_movies_by_format():
    format_id = int(input("Format ID: "))
    format = db.get_format(format_id)
    if format == None:
        print("There is no format with that ID.\n")
    else:
        print()
        movies = db.get_movies_by_format(format_id)
        display_movies(movies, format.name.upper())

#DISPLAY BY YEAR
    
def display_books_by_year():
    year = int(input("Year: "))
    print()
    books = db.get_books_by_year(year)
    display_books(books, str(year))

def display_movies_by_year():
    year = int(input("Year: "))
    print()
    movies = db.get_movies_by_year(year)
    display_movies(movies, str(year))

def display_tv_by_year():
    year = int(input("Year: "))
    print()
    tv = db.get_tv_by_year(year)
    display_tv(tv, str(year))

#DISPLAY BY LENGTH

def display_movies_by_minutes():
    minutes_given = int(input("Maximum number of minutes: "))
    print()
    movies = db.get_movies_by_minutes(minutes_given)
    display_movies(movies, "LESS THAN " + str(minutes_given) + " MINUTES")


#ADD TO DATABASE

def add_book():
    title       = input("Title: ")
    year        = int(input("Year: "))
    authors     = input("Authors: ")
    genre_id = int(input("Genre ID: "))
    format_id   = int(input("Format ID: "))
    
    genre = db.get_genre(genre_id)
    format = db.get_format(format_id)
    if genre == None:
        print("There is no genre with that ID. Book NOT added.\n")
    elif format == None:
        print("There is no format with that ID.  Book NOT added.\n")
    elif format.type != "book":
        print("You entered the wrong format type.  Book NOT added.\n")
    else:        
        book = Book(title=title, year=year, authors=authors,
                      genre=genre, format=format)
        db.add_book(book)    
        print(title + " was added to database.\n")

def add_movie():
    title       = input("Title: ")
    year        = int(input("Year: "))
    minutes     = int(input("Minutes: "))
    genre_id    = int(input("Genre ID: "))
    format_id   = int(input("Format ID: "))
    
    genre = db.get_genre(genre_id)
    format = db.get_format(format_id)
    if genre == None:
        print("There is no genre with that ID. Movie NOT added.\n")
    elif format == None:
        print("There is no format with that ID.  Movie NOT added.\n")
    elif format.type != "video":
        print("You entered the wrong format type.  Movie NOT added.\n")
    else:        
        movie = Movie(title=title, year=year, minutes=minutes,
                      genre=genre, format=format)
        db.add_movie(movie)    
        print(title + " was added to database.\n")

#DELETE FROM DATABASE

def delete_book():
    book_id = int(input("Book ID: "))
    book = db.get_book(book_id)
    choice = input("Are you sure that you want to delete '" + book.title + "'? (y/n): ")
    if choice == "y":
        db.delete_book(book_id)
        print("'" + book.title + "' was deleted from the database. \n")
    else:
        print("'" + book.title + "' was NOT deleted from the database. \n")

def delete_movie():
    movie_id = int(input("Movie ID: "))
    movie = db.get_movie(movie_id)
    choice = input("Are you sure that you want to delete '" + movie.title + "'? (y/n): ")
    if choice == "y":
        db.delete_movie(movie_id)
        print("'" + movie.title + "' was deleted from the database. \n")
    else:
        print("'" + movie.title + "' was NOT deleted from the database. \n")

#VIEWING SHARED MEDIA

def view_shared_books():
    print()
    books = db.get_shared_books()
    display_books(books, "SHARED")

def view_shared_movies():
    print()
    movies = db.get_shared_movies()
    display_movies(movies, "SHARED")

#MAIN
        
def main():
    db.connect()
    display_main_menu()
    while True:
        command = input("Command: ")
        if command == "1":
            movie_menu()
        elif command == "2":
            book_menu()
        #elif command == "3":
        #    tv_menu()
        elif command == "0":
            break
        else:
            print("Not a valid command.  Please try again. \n")
            display_main_menu
    db.close()

if __name__ == "__main__":
    main()
