from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
@app.route("/index")
def main():
	categories = {'Villagers', 'Furniture'}
	filters = {'Cool', 'Cute', 'Harmonious', 'Hip', 'Natural', 'Rustic', 'Sporty'}
	return render_template('index.html', categories=categories, filters=filters)
if __name__ == "__main__":
    app.run()
