#This is a web scraper using beautiful 
#soup and some other library called urllib

#the web scraper is trying to get all text #from an article

from bs4 import BeautifulSoup
from bs4.element import Comment 
import urllib.request

def tag_visible(element):
	if element.parent.name in ['style','script','head','title','meta','[document]']:
		return False

	if isinstance(element,Comment):
		return False

	return True

def text_from_html(body):
	soup = BeautifulSoup(body,'html.parser')
	texts=soup.findAll(text=True)
	visible_texts=filter(tag_visible,texts)
	return u"".join(t.strip() for t in visible_texts)


url=input("Enter Url : ")
html=urllib.request.urlopen(url).read()
print(text_from_html(html))
