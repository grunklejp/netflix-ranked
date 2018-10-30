#flask server
from flask import Flask, render_template
import sqlite3
from moviec import Movie
from access_db import getMovies

class Config(object):
    # ...
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')

app = Flask(__name__)
currentpage = 1
DATABASE_URL = "rankedmovies.db"



@app.route('/')
def helloworld():
	nlist = getMovies(currentpage)
	return render_template('main.html', nlist = nlist)

@app.route('/<currentpage>')
def next():
	global currentpage
	currentpage += 1

	nlist = getMovies(currentpage)
	return render_template('main.html', nlist= nlist)

@app.route('/p/<currentpage>')
def prev():
	global currentpage
	currentpage -= 1

	nlist = getMovies(currentpage)
	return render_template('main.html', nlist= nlist)




if __name__ == '__main__':
	app.run()



