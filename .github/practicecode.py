import requests 
url = "https://saeedghani.pk/"
r = requests.get(url)
print (r.text)