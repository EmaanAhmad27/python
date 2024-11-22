import requests 
from bs4 import BeautifulSoup
url = "https://saeedghani.pk/"
r = requests.get(url)
soup = BeautifulSoup(r.text, "lxml")
# print (soup.div)

#tag = soup.header
#print (tag.attrs)

