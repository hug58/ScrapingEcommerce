
import requests
import json
import re
import os.path

from bs4 import BeautifulSoup
from common import config


class Page:
	def __init__(self,new_site_uid,url):

		self._config = config()[new_site_uid]
		self._queries = self._config['queries']
		self._page_content = None

		self._visit(url)


	def _visit(self,url):
		

		try:
			html = requests.get(url).text
			self._page_content =  BeautifulSoup(html,"html.parser")
		
		except requests.ConnectionError as e:
			print(e)






class Ecommerce(Page):
	def __init__(self,new_site_uid,url):

		Page.__init__(self,new_site_uid,url)

		self._data = None

		self._name = None
		self._price = None
		self._available = None
		self._image = None

		self._data = self.__data()


	def __data(self):

		#convierto el objeto tag en un texto para poder manipularlo con regex
		_data = str(self._page_content.find(self._queries["data"]["tag"],type=self._queries["data"]["type"]))

		pattern = r"\<script.+\>((\n|.)+)\<\/script\>"
		result =re.search(pattern,_data,re.MULTILINE)

		
		"""	Accede al segundo grupo del patron, de esta forma
			divido la cadena
		"""		
		data = json.loads(result.group(1))

		return data

	@property
	def name(self):

		self._name = self._data["name"]
		return self._name
	

	@property
	def price(self):
		self._price = self._data["offers"]["price"]
		priceCurrency = self._data["offers"]["priceCurrency"]
		return (self._price,priceCurrency)

	@property
	def available(self):
		return self.available
	

	@property
	def image(self):

		path = 'data/images'

		url_image = self._data["image"]
		if not os.path.isdir(path):
			os.makedirs(path, exist_ok=True)

		with requests.get(url_image,stream=True) as r:
			r.raise_for_status()
			filename = os.path.join('data/images',self._data['name'])

			with open(f"{filename}.jpg",'wb') as f:
				for chunk in r.iter_content(1024):
					if chunk:
						f.write(chunk)



		self._image = url_image

		return self._image
	
	
	
