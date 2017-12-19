#"""
#Routes and views for the flask application.
#"""

import ui
import db
import sqlite3
from datetime import datetime
from flask import Flask, flash, redirect, render_template, request, session, abort, jsonify, json
#from MediaSN import app

app = Flask(__name__)

@app.route('/')
def home():
#    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/movies')
def movies():
#    """Renders the movie page."""
    print()
    db.connect()
    #movies = db.get_all_movies()
    movie = db.get_movie_dict(1)
    return json.dumps(movie)
    db.close()
    #return render_template(
    #    'movies.html',
    #    title='Movies',
    #    year=datetime.now().year,
    #    message='Your movie page.'
    #)

@app.route('/tv')
def tv():
#    """Renders the contact page."""
    return render_template(
        'tv.html',
        title='TV',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/books')
def books():
#    """Renders the books page."""
    print()
    db.connect()
    book = db.get_book_dict(1)
    return jsonify(book)
    db.close()
    #return render_template(
    #    'books.html',
    #    title='Books',
    #    year=datetime.now().year,
    #    message='Your contact page.'
    #)

@app.route('/contact')
def contact():
#    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
#    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

#def jdefault(o):
#    return o.__dict__
 
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
    db.connect()