from nflix_scraper import getRatings, sortMovies
import sqlite3

movielist = getRatings()

conn = sqlite3.connect('rankedmovies.db')
c = conn.cursor()
c.execute("CREATE TABLE allmovies (title text, imdb_rating text, rt_rating text, mc_rating text, avg_rating real, minID int, maxID int)")


for movie in movielist:
	c.execute("INSERT INTO allmovies VALUES (?, ?, ?, ?, ?, ?, ?)",
		     (movie.title, movie.imdb_rating, movie.rt_rating, movie.mc_rating, movie.average_rating, movie.minID, movie.maxID))



conn.commit()

conn.close()