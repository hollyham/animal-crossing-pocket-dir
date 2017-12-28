import requests
from bs4 import BeautifulSoup

url = 'http://animalcrossing.wikia.com/wiki/Villager_list_(Pocket_Camp)'
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
web_table = soup.find('table', class_='roundy sortable')
villagers = web_table.find_all('tr')
for animal in villagers[1:]:# Skips 0 index (table header)
    try:
        current = animal.find('a')
        print(current.get_text())
        count += 1
    except AttributeError:
        print("AttributeError")
