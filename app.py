from flask import Flask, render_template
import json
app = Flask(__name__)

with open('static/data/villagers.json') as file:
	villager_by_type = json.load(file)
with open('static/data/filters.json') as file:
	filters = json.load(file)

categories = {'Villagers': 'villagers_table', 'Furniture': 'furniture_table'}

@app.route("/")
@app.route("/index")
def main():
	return render_template('index.html', categories=categories, filters=filters)
if __name__ == "__main__":
    app.run()
