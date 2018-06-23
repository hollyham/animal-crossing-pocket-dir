import csv
import requests
from bs4 import BeautifulSoup

url = 'http://animalcrossing.wikia.com/wiki/Villager_list_(Pocket_Camp)'
page = requests.get(url)
page.encoding ="utf-8"

soup = BeautifulSoup(page.content, 'html.parser')

# Scrapes villager data

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

print("Villagers Scraped Successfully")

# Scrapes amenities data

url = 'http://animalcrossing.wikia.com/wiki/Amenities'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

web_table = soup.findAll('table', class_='roundy')[2] # Finds amenities table
amenities = web_table.find('tr') # Gets rows of the table
amenities = amenities.find('table').findAll('tr') # Find inncer content table


full_data=[] # Amenities with data
amenity_data=[] # Data for each amenity 
for item in amenities[1:]: # Skips 0 index (table header)
    if not item.find_all('th'): # Detects headers and skips them
        data = item.find_all('td')

        try:
            name = data[0].get_text() # Name of amenity
            print(data[0].get_text())
            image = data[1].find('a', href=True)['href']

            materials_list = []
            materials = data[2].find_all('a')
            print(data[2].get_text())

#        personality = data[2].find('a').get_text()[2:]
#        species = data[3].find('a').get_text()
#        birthday = data[4].get_text().strip()
#        catchphrase = data[5].get_text().strip()
#        theme = data[6].get_text().strip()

#        amenity_data.extend([name,image,personality,species,birthday,catchphrase,theme])

#        resources_list = []
#        resources = data[7].find_all('a')

#        for resource in resources:
#            resources_list.append(resource.get_text())
         
#        resources_str = ", ".join(resources_list)
#        villager_data.append(resources_str)

        except AttributeError:
            print("Name not found")

    else:
        print("Found header")
#    full_data.append(villager_data[:])
#    del villager_data[:] #equivalent to villager_data.clear()
#with open("./villagers.csv", "w") as outfile:
#    writer= csv.writer(outfile)
#    for row in full_data:
#        writer.writerow(row)