import requests
from bs4 import BeautifulSoup

url = 'http://dataquestio.github.io/web-scraping-pages/simple.html' 
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
html = list(soup.children)[2] # Selects contents of html tag
body = list(html.children)[3] # Selects body of html
p = list(body.children)[1] # Selects contents of p tag
print(p.get_text()) # Isolates text inside tag

