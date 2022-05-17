import requests
from bs4 import BeautifulSoup

url = "http://www.google.com"

r = requests.get(url)
s = BeautifulSoup(r.content)
print(s.prettify())