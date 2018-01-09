import csv
import requests
from bs4 import BeautifulSoup

url = 'http://animalcrossing.wikia.com/wiki/Villager_list_(Pocket_Camp)'
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
web_table = soup.find('table', class_='roundy sortable') # Finds villager table
villagers = web_table.find_all('tr') # Gets rows of the table

villager_data=[] # Data for each villager 
for animal in villagers[1:]:# Skips 0 index (table header)
    data = animal.find_all('td')
    try:
        name = data[0].find('a') # Name of villager (name is link to villager's wiki)
        print(name.get_text())
        image = data[1].find('a', href=True) 
        print(image['href'])
        personality = data[2].find('a').get_text()
        print(personality)
        species = data[3].find('a').get_text()
        print(species)
        birthday = data[4].get_text()
        print(birthday)
        catchphrase = data[5].get_text()
        print(catchphrase)
        theme = data[6].get_text()
        print(theme)
        resources_list = []
        resources = data[7].find_all('a')
        for resource in resources:
            resources_list.append(resource.get_text())
            print(resource.get_text())
        

#villager_data=[name,image.get('href')]
    except AttributeError:
        print("Name not found")

#with open("./villagers.csv", "wb") as outfile:
#    writer= csv.writer(outfile)
#    for row in data_list:
#        writer.writerow(row)
