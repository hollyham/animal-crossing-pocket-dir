import csv
import requests
from bs4 import BeautifulSoup

url = 'http://animalcrossing.wikia.com/wiki/Villager_list_(Pocket_Camp)'
page = requests.get(url)
page.encoding ="utf-8"

soup = BeautifulSoup(page.content, 'html.parser')
web_table = soup.find('table', class_='roundy sortable') # Finds villager table
villagers = web_table.find_all('tr') # Gets rows of the table

full_data=[] # Villagers with data
villager_data=[] # Data for each villager 
for animal in villagers[1:]:# Skips 0 index (table header)
    data = animal.find_all('td')

    try:
        name = data[0].find('a').get_text() # Name of villager (name is link to villager's wiki)
        image = data[1].find('a', href=True)['href']
        personality = data[2].find('a').get_text()[2:]
        species = data[3].find('a').get_text()
        birthday = data[4].get_text().strip()
        catchphrase = data[5].get_text().strip()
        theme = data[6].get_text().strip()

        villager_data.extend([name,image,personality,species,birthday,catchphrase,theme])

        resources_list = []
        resources = data[7].find_all('a')

        for resource in resources:
            resources_list.append(resource.get_text())
         
        resources_str = ", ".join(resources_list)
        villager_data.append(resources_str)

    except AttributeError:
        print("Name not found")
    full_data.append(villager_data[:])
    del villager_data[:] #equivalent to villager_data.clear()
with open("./villagers.csv", "w") as outfile:
    writer= csv.writer(outfile)
    for row in full_data:
        writer.writerow(row)
