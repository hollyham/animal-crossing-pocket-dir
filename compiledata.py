import json
import os
from sqlalchemy import Column, Integer, String, create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine import reflection

engine = create_engine(os.environ['DATABASE_URL']) # object to communicate with database
Base = declarative_base(engine)
metadata = MetaData()
metadata.reflect(engine)

Session = sessionmaker(bind=engine) # handle to the database
session = Session()

# Model for villagers_table
class Villager(Base):
	__tablename__ = 'villagers_table'
	id = Column(Integer, primary_key=True)
	name = Column(String)
	image_url = Column(String)
	personality = Column(String)
	species = Column(String)
	birthday = Column(String)
	catchphrase = Column(String)
	type = Column(String)
	resources = Column(String) 

# Creates dictionary of villagers based on their type
villagers = {}
for villager in session.query(Villager).all():
	if(villager.type in villagers):
		villagers[villager.type].append(villager.name)
	else:
		villagers[villager.type] = [villager.name]

# Creates dictionary of types of filters for villagers (TODO: Furnitrue and amenities)
villagers_filters = {}
for category in metadata.tables.keys():
	if(category == "villagers_table"):
		villagers_filters[category] = list(villagers)

# create json files with dictionaries
with open('static/data/villagers.json', 'w') as file:
	json.dump(villagers, file)
with open('static/data/villagers-filters.json', 'w') as file:
	json.dump(villagers_filters, file)