import sqlite3
from moviec import Movie

def getMovies(page):
	conn = sqlite3.connect('rankedmovies.db')
	c = conn.cursor()
	ceil = page*20
	floor = ceil - 20
	nlist = []
	for row in c.execute('SELECT * FROM allmovies WHERE maxID < ? AND maxID > ? ORDER BY maxID', (ceil, floor)):
		movie = Movie(row[0])
		movie.imdb_rating = row[1]
		movie.rt_rating = row[2]
		movie.mc_rating = row[3]
		movie.minID = row[5]
		movie.maxID = row[6]

		nlist.append(movie)

	conn.close()
	return nlist