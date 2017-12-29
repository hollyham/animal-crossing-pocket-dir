import requests
from bs4 import BeautifulSoup

url = 'http://animalcrossing.wikia.com/wiki/Villager_list_(Pocket_Camp)'
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
web_table = soup.find('table', class_='roundy sortable')
villagers = web_table.find_all('tr')
for animal in villagers[1:]:# Skips 0 index (table header)
    data = animal.find_all('td')
    try:
        current = data[0].find('a')
        print(current.get_text())
        image = data[1].find('a', href=True)
        print(image['href'])
    except AttributeError:
        print("Name not found")
