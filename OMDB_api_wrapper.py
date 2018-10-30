#
#simple movie database api wrapper function
#get key at http://www.omdbapi.com/apikey.aspx
#6ea98f27
import requests

class OMDb:
	def __init__(self, key):
		self.omdb_key = key
		self.urlkey_text = '&apikey='+key
		self.base_url = 'http://www.omdbapi.com/?'


	def get_movie(self, title):
		fmt_title = title.replace(' ', '+')
		server = requests.get(self.base_url + 't=' + fmt_title+self.urlkey_text)
		return server.json()


#db = OMDb('6ea98f27')
#mv =db.get_movie('Law and order')
#print(mv['Ratings'])
