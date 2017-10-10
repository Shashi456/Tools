import requests
from bs4 import BeautifulSoup

# I am building a scraper for Wired.com
"""Writing any scraper first involves looking at the site 
and recognising it's elements """
# get the url from the user
s=input("Input URL: ")
print(s)
# the requests module gets the data from the url

r= requests.get(s)
#beautiful soup is for extracting html and xml data 
# sort of beautification of the data scrapped
soup =BeautifulSoup(r.content)
# In wired.com data we want is present in the article tag and hence 
#we are scraping the same 

for data in soup.find_all("p"):
	print(data.text)



