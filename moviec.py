

class Movie:

	def __init__(self, title):
		self.title = title
		self.imdb_rating = None
		self.rt_rating = None
		self.mc_rating = None
		self.image_url = None
		self.minID = None
		self.maxID =None
		

	@property
	def imdb_percent(self):
		dec_rate = self.imdb_rating.split('/')
		return int(float(dec_rate[0]) * 10)

	@property
	def rt_percent(self):
		rate = self.rt_rating.split('%')
		return int(rate[0])


	@property	
	def mc_percent(self):
		rate = self.mc_rating.split('/')
		return int(rate[0])	
	'''
	@image_url.setter
	def image_url(self, image):
		self.image_url = image

	'''

	@property
	def average_rating(self):
		if (self.imdb_rating != None) and (self.rt_rating == None) and (self.mc_rating == None):
			return self.imdb_percent
		elif (self.imdb_rating != None) and (self.rt_rating != None) and (self.mc_rating == None):
			return round((self.imdb_percent + self.rt_percent) / 2, 2)
		elif (self.imdb_rating != None) and (self.rt_rating == None) and (self.mc_rating != None):
			return round((self.imdb_percent + self.mc_percent) / 2, 2)
		elif (self.imdb_rating == None) and (self.rt_rating != None) and (self.mc_rating == None):
			return self.rt_percent
		elif (self.imdb_rating == None) and (self.rt_rating == None) and (self.mc_rating != None):
			return self.mc_percent	
		elif (self.imdb_rating == None) and (self.rt_rating != None) and (self.mc_rating != None):
			return round((self.mc_percent + self.rt_percent) /2, 2)
		elif (self.imdb_rating != None) and (self.rt_rating != None) and (self.mc_rating != None):
			return round((self.imdb_percent + self.mc_percent + self.rt_percent) / 3, 2)
		else:
			return 0
		

	def __str__(self):
		return '''{}\n\tIMDB : {}\n\tRotten Tomatoes : {}\n\tMetacritic :
			   {}\n\tAverage Rating: {} min:{}\n\tmax:{}\n\t'''.format(self.title, 
																	  self.imdb_rating, 
																	  self.rt_rating,
																	  self.mc_rating,
																	  self.average_rating,
																	  self.minID,
																	  self.maxID)
