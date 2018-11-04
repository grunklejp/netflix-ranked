#flask server
from flask import Flask, render_template
import sqlite3
from moviec import Movie
from access_db import getMovies
import os


SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
app = Flask(__name__)
DATABASE_URL = "rankedmovies.db"


@app.route('/')
def helloworld():
	current_pg = 1
	nlist = getMovies(current_pg)
	return render_template('main.html', nlist=nlist, current_pg=current_pg)

@app.route('/<int:current_pg>')
def next(current_pg):
	current_pg += 1

	nlist = getMovies(current_pg)
	return render_template('main.html', nlist= nlist, current_pg=current_pg)

@app.route('/p/<int:current_pg>')
def prev(current_pg):
	current_pg -= 1

	nlist = getMovies(current_pg)
	return render_template('main.html', nlist= nlist, current_pg=current_pg)


if __name__ == '__main__':
	app.run()



