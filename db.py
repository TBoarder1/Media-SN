import sys
import os
import sqlite3
from contextlib import closing

from objects import Format
from objects import Genre
from objects import Book
from objects import Movie
from objects import TV

conn = None
#conn = sqlite3.connect("media.sqlite")

def connect():
    global conn
    if not conn:
        if sys.platform == "win32":
            DB_FILE = "C:/Users/Tracy/Documents/School/Semester 10/Python Programming/python_allfiles/murach/python/_db/media.sqlite"
        else:
            HOME = os.environ["HOME"]
            DB_FILE = HOME + "/Documents/murach/python/_db/media.sqlite"
        
        conn = sqlite3.connect("media.sqlite")
        conn.row_factory = sqlite3.Row

def close():
    if conn:
        conn.close()

def make_format(row):
    return Format(row["formatID"], row["formatName"], row["formatType"])

def make_genre(row):
    return Genre(row["genreID"], row["genreName"])

def make_book(row):
    return Book(row["bookID"], row["title"], row["year"], row["authors"],
            make_genre(row), make_format(row))

def make_movie(row):
    return Movie(row["movieID"], row["title"], row["year"], row["minutes"],
            make_genre(row), make_format(row))

def make_movie_dict(movie):
    #movie_dict = [["MovieID", movie[0]]
    #              ["Title", movie[1]]
    #              ["Year", movie[2]]
    #              ["Minutes", movie[3]]
    #              ["Genre", movie[4]]
    #              ["Format", movie[5]]]
    #movie_dict = dict(movie_dict)
    movie_dict = {"movieID":"Movieid", "Title":"MovieTitle", "Year":"MovieYear"}
    return movie_dict

def make_book_dict(book):
    #movie_dict = [["MovieID", movie[0]]
    #              ["Title", movie[1]]
    #              ["Year", movie[2]]
    #              ["Minutes", movie[3]]
    #              ["Genre", movie[4]]
    #              ["Format", movie[5]]]
    #movie_dict = dict(movie_dict)
    book_dict = {"bookID":"Bookid", "Title":"BookTitle", "Year":"BookYear"}
    return book_dict

#GET ALL

def get_all_books():
    query = '''SELECT bookID, Book.title, year, authors,
                      Book.genreID as genreID,
                      Genre.name as genreName,
                      Book.formatID as formatID,
                      Format.name as formatName,
                      Format.type as formatType
               FROM Book JOIN Genre ON Book.genreID = Genre.genreID
                         JOIN Format ON Book.formatID = Format.formatID
               ORDER BY Book.title ASC'''
    with closing(conn.cursor()) as c:
        c.execute(query, ())
        results = c.fetchall()

    books = []
    for row in results:
        books.append(make_book(row))
    return books

def get_all_movies():
    query = '''SELECT movieID, Movie.title, year, minutes,
                      Movie.genreID as genreID,
                      Genre.name as genreName,
                      Movie.formatID as formatID,
                      Format.name as formatName,
                      Format.type as formatType
               FROM Movie JOIN Genre ON Movie.genreID = Genre.genreID
                          JOIN Format ON Movie.formatID = Format.formatID
               ORDER BY Movie.title ASC'''
    with closing(conn.cursor()) as c:
        c.execute(query, ())
        results = c.fetchall()

    movies = []
    for row in results:
        movies.append(make_movie(row))
    return movies

def get_all_movies_dict():
    query = '''SELECT movieID, Movie.title, year, minutes,
                      Movie.genreID as genreID,
                      Genre.name as genreName,
                      Movie.formatID as formatID,
                      Format.name as formatName,
                      Format.type as formatType
               FROM Movie JOIN Genre ON Movie.genreID = Genre.genreID
                          JOIN Format ON Movie.formatID = Format.formatID
               ORDER BY Movie.title ASC'''
    with closing(conn.cursor()) as c:
        c.execute(query, ())
        results = c.fetchall()

    movies = []
    for row in results:
        movies.append(make_movie(row))
        make_movie_dict(movies)
    return movies

#GET FORMATS

def get_formats():
    query = '''SELECT formatID, name as formatName, type as formatType
               FROM Format'''
    with closing(conn.cursor()) as c:
        c.execute(query)
        results = c.fetchall()

    formats = []
    for row in results:
        formats.append(make_format(row))
    return formats

def get_format(format_id):
    query = '''SELECT formatID, name as formatName, type as formatType
               FROM Format WHERE formatID = ?'''
    with closing(conn.cursor()) as c:
        c.execute(query, (format_id,))
        row = c.fetchone()
        if row:
            return make_format(row)
        else:
            return None

def get_books_by_format(format_id):
    query = '''SELECT bookID, Book.title, year, authors,
                      Book.genreID as genreID,
                      Genre.name as genreName,
                      Book.formatID as formatID,
                      Format.name as formatName
               FROM Book JOIN Genre ON Book.genreID = Genre.genreID
                         JOIN Format ON Book.formatID = Format.formatID  
               WHERE Book.formatID = ?'''
    with closing(conn.cursor()) as c:
        c.execute(query, (format_id,))
        results = c.fetchall()

    books = []
    for row in results:
        books.append(make_book(row))
    return books

def get_movies_by_format(format_id):
    query = '''SELECT movieID, Movie.title, year, minutes,
                      Movie.genreID as genreID,
                      Genre.name as genreName,
                      Movie.formatID as formatID,
                      Format.name as formatName,
                      Format.type as formatType
               FROM Movie JOIN Genre ON Movie.genreID = Genre.genreID
                          JOIN Format ON Movie.formatID = Format.formatID  
               WHERE Movie.formatID = ?'''
    with closing(conn.cursor()) as c:
        c.execute(query, (format_id,))
        results = c.fetchall()

    movies = []
    for row in results:
        movies.append(make_movie(row))
    return movies

#GET GENRES

def get_genres():
    query = '''SELECT genreID, name as genreName
               FROM Genre'''
    with closing(conn.cursor()) as c:
        c.execute(query)
        results = c.fetchall()

    genres = []
    for row in results:
        genres.append(make_genre(row))
    return genres

def get_genre(genre_id):
    query = '''SELECT genreID, name as genreName
               FROM Genre WHERE genreID = ?'''
    with closing(conn.cursor()) as c:
        c.execute(query, (genre_id,))
        row = c.fetchone()
        if row:
            return make_genre(row)
        else:
            return None

def get_books_by_genre(genre_id):
    query = '''SELECT bookID, Book.title, year, authors,
                      Book.genreID as genreID,
                      Genre.name as genreName,
                      Book.formatID as formatID,
                      Format.name as formatName,
                      Format.type as formatType
               FROM Book JOIN Genre ON Book.genreID = Genre.genreID
                         JOIN Format ON Book.formatID = Format.formatID
               WHERE Book.genreID = ?'''
    with closing(conn.cursor()) as c:
        c.execute(query, (genre_id,))
        results = c.fetchall()

    books = []
    for row in results:
        books.append(make_book(row))
    return books

def get_movies_by_genre(genre_id):
    query = '''SELECT movieID, Movie.title, year, minutes,
                      Movie.genreID as genreID,
                      Genre.name as genreName,
                      Movie.formatID as formatID,
                      Format.name as formatName,
                      Format.type as formatType
               FROM Movie JOIN Genre ON Movie.genreID = Genre.genreID
                          JOIN Format ON Movie.formatID = Format.formatID 
               WHERE Movie.genreID = ?'''
    with closing(conn.cursor()) as c:
        c.execute(query, (genre_id,))
        results = c.fetchall()

    movies = []
    for row in results:
        movies.append(make_movie(row))
    return movies

#GET BY YEAR

def get_books_by_year(year):
    query = '''SELECT bookID, Book.title, year, authors,
                      Book.genreID as genreID,
                      Genre.name as genreName,
                      Book.formatID as formatID,
                      Format.name as formatName
               FROM Book JOIN Genre ON Book.genreID = Genre.genreID
                         JOIN Format ON Book.formatID = Format.formatID  
               WHERE year = ?'''
    with closing(conn.cursor()) as c:
        c.execute(query, (year,))
        results = c.fetchall()

    books = []
    for row in results:
        books.append(make_book(row))
    return books

def get_movies_by_year(year):
    query = '''SELECT movieID, Movie.title, year, minutes,
                      Movie.genreID as genreID,
                      Genre.name as genreName,
                      Movie.formatID as formatID,
                      Format.name as formatName
               FROM Movie JOIN Genre ON Movie.genreID = Genre.genreID
                          JOIN Format ON Movie.formatID = Format.formatID
               WHERE year = ?'''
    with closing(conn.cursor()) as c:
        c.execute(query, (year,))
        results = c.fetchall()

    movies = []
    for row in results:
        movies.append(make_movie(row))
    return movies

#GET BY LENGTH

def get_movies_by_minutes(minutes_given):
    query = '''SELECT movieID, Movie.title, year, minutes,
                      Movie.genreID as genreID,
                      Genre.name as genreName,
                      Movie.formatID as formatID,
                      Format.name as formatName,
                      Format.type as formatType
               FROM Movie JOIN Genre ON Movie.genreID = Genre.genreID
                          JOIN Format ON Movie.formatID = Format.formatID
               WHERE minutes < ?
               ORDER BY minutes ASC'''
    with closing(conn.cursor()) as c:
        c.execute(query, (minutes_given,))
        results = c.fetchall()

    movies = []
    for row in results:
        movies.append(make_movie(row))
    return movies

#ADD TO DATABASE

def add_book(book):
    sql = '''INSERT INTO Book (genreID, formatID title, year, authors) 
             VALUES (?, ?, ?, ?, ?)'''
    with closing(conn.cursor()) as c:
        c.execute(sql, (book.genre.id, book.format.id, book.title, book.year,
                        book.authors))
        conn.commit()

def add_movie(movie):
    sql = '''INSERT INTO Movie (genreID, formatID, title, year, minutes) 
             VALUES (?, ?, ?, ?, ?)'''
    with closing(conn.cursor()) as c:
        c.execute(sql, (movie.genre.id, movie.format.id, movie.title, movie.year,
                        movie.minutes))
        conn.commit()

#DELETE FROM DATABASE

def delete_book(book_id):
    sql = '''DELETE FROM Book WHERE bookID = ?'''
    with closing(conn.cursor()) as c:
        c.execute(sql, (book_id,))
        test = conn.commit()
        print("Test", test)

def delete_movie(movie_id):
    sql = '''DELETE FROM Movie WHERE movieID = ?'''
    with closing(conn.cursor()) as c:
        c.execute(sql, (movie_id,))
        test = conn.commit()
        print("Test", test)

#GET SHARED

def get_shared_books():
    query = '''SELECT Book.bookID, Book.title, Book.year, Book.authors,
                          Book.genreID as genreID,
                          Genre.name as genreName,
                          Book.formatID as formatID,
                          Format.name as formatName,
                          Format.type as formatType
                   FROM Book JOIN Genre ON Book.genreID = Genre.genreID
                             JOIN Format ON Book.formatID = Format.formatID
                             INNER JOIN FriendsBooks ON Book.title = FriendsBooks.title'''
    with closing(conn.cursor()) as c:
            c.execute(query, ())
            results = c.fetchall()

    books = []
    for row in results:
        books.append(make_book(row))
    return books

def get_shared_movies():
    query = '''SELECT Movie.movieID, Movie.title, Movie.year, Movie.minutes,
                      Movie.genreID as genreID,
                      Genre.name as genreName,
                      Movie.formatID as formatID,
                      Format.name as formatName,
                      Format.type as formatType
               FROM Movie JOIN Genre ON Movie.genreID = Genre.genreID
                          JOIN Format ON Movie.formatID = Format.formatID
                          INNER JOIN FriendsMovies ON Movie.title = FriendsMovies.title'''
    with closing(conn.cursor()) as c:
        c.execute(query, ())
        results = c.fetchall()

    movies = []
    for row in results:
        movies.append(make_movie(row))
    return movies

#GET FROM DATABASE

def get_book(book_id):
    query = '''SELECT bookID, Book.title, year, authors,
                      Book.genreID as genreID,
                      Genre.name as genreName,
                      Book.formatID as formatID,
                      Format.name as formatName,
                      Format.type as formatType
               FROM Book JOIN Genre ON Book.genreID = Genre.genreID
                         JOIN Format ON Book.formatID = Format.formatID   
               WHERE bookID = ?'''
    with closing(conn.cursor()) as c:
        c.execute(query, (book_id,))
        row = c.fetchone()
    
    book = []
    book = make_book(row)
    return book

def get_movie(movie_id):
    query = '''SELECT movieID, Movie.title, year, minutes,
                      Movie.genreID as genreID,
                      Genre.name as genreName,
                      Movie.formatID as formatID,
                      Format.name as formatName,
                      Format.type as formatType
               FROM Movie JOIN Genre ON Movie.genreID = Genre.genreID
                          JOIN Format ON Movie.formatID = Format.formatID
               WHERE movieID = ?'''
    with closing(conn.cursor()) as c:
        c.execute(query, (movie_id,))
        row = c.fetchone()

    movie = []
    movie = make_movie(row)
        
    return movie

def get_movie_dict(movie_id):
    movie = get_movie(movie_id)
    movie_dict = make_movie_dict(movie)
    return movie_dict

def get_book_dict(book_id):
    book = get_book(book_id)
    book_dict = make_book_dict(book)
    return book_dict
