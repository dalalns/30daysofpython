#pip install requests
#pip install html5lib
#pip install bs4
#Furthur to study
#1. Python for web applications using Flask and Django
#2. Python for DB related applications. Raw queries and ORMs
#3. Python for data science using Pandas, Numpy and Scipy
#https://www.digitalocean.com/community/tutorials/how-to-scrape-web-pages-with-beautiful-soup-and-python-3
import requests
from bs4 import BeautifulSoup
import lxml
import csv

import requests
from bs4 import BeautifulSoup


# Collect and parse first page
page = requests.get('https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ1.htm')
soup = BeautifulSoup(page.text, 'html.parser')

# Remove bottom links
last_links = soup.find(class_='AlphaNav')
last_links.decompose()

# Pull all text from the BodyText div
artist_name_list = soup.find(class_='BodyText')

# Pull text from all instances of <a> tag within BodyText div
artist_name_list_items = artist_name_list.find_all('a')

for artist_name in artist_name_list_items:
    #print(artist_name.prettify())
	print(artist_name.contents[0])