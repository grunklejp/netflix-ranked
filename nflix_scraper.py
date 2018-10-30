#TODO: 
#store image 
# add sqlite3 to store  



#scraper

from bs4 import BeautifulSoup
import requests, time, json
from string import printable
from OMDB_api_wrapper import OMDb
from moviec import Movie   


def get_nflix_lib():

	num_pages = 44
	current_page = 1
	offset = 150
	lib = []
	site = 'https://reelgood.com/source/netflix'
	bullshit = 'df'

	#gets titles from first page
	source = requests.get(site).text
	soup = BeautifulSoup(source, 'html.parser')
	contents = soup.find_all('td', class_=bullshit)
	
	for element in contents:
		newlist = str(element).split('>')
		newlist = newlist[2].split('<')
		lib.append(newlist[0].replace('&amp;', 'and'))

	

	#gets titles from the rest
	while current_page < num_pages:
		source = requests.get(site +'?offset='+str(offset)).text
		soup = BeautifulSoup(source, 'html.parser')
		contents =soup.find_all('td', class_=bullshit)
		
		for element in contents:
			newlist = str(element).split('>')
			newlist = newlist[2].split('<')
			title = ''.join(char for char in newlist[0] if char in printable)
			lib.append(title.replace('&amp;', 'and'))
	

		offset = offset + 100
		current_page += 1 

	print(len(lib))
	return lib

		
def getRatings():
	netflix_list = get_nflix_lib()
	db = OMDb('6ea98f27')
	ranked_titles = []
	title_errors = []

	for title in netflix_list:
		try:

			movie_holder = db.get_movie(title)
			if movie_holder['Response'] == 'True':
				movie = Movie(title)

				for rankings in movie_holder['Ratings']:
					if rankings['Source'] == 'Internet Movie Database':
						movie.imdb_rating = rankings['Value']
					elif rankings['Source'] == 'Rotten Tomatoes':
						movie.rt_rating = rankings['Value']
					elif rankings['Source'] == 'Metacritic':
						movie.mc_rating = rankings['Value']
				
				ranked_titles.append(movie)

		except Exception:
			title_errors.append(title)			

	print('Entries: {}'.format(len(ranked_titles)))
	print(title_errors)


	return sortMovies(ranked_titles)

# revTF == boolean True == low to high
def sortMovies(r_list):

	#sets minIDs
	temp = sorted(r_list, key=lambda item_in_list: item_in_list.average_rating, reverse=True)
	for i in range(0, len(temp)):
		temp[i].minID = i

	#sets maxIDs
	temp = sorted(r_list, key=lambda item_in_list: item_in_list.average_rating, reverse=False)
	for i in range(0, len(temp)):
		temp[i].maxID = i

	return r_list


if __name__ == "__main__":
	titles = getRatings()

	for i in titles:
		print(i)
