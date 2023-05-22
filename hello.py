from flask import Flask, render_template, request, redirect, url_for, session
from db import get_records_by_year_and_bech_rating

app = Flask(__name__)

# homepage route
@app.route('/')
def homepage():
    return render_template('index.html')

# search bar route
@app.route('/search')
def search():
    return render_template('search.html')

# account login route
@app.route('/savedplaylists', methods=["POST", "GET"])
def playlists():
    name = request.form["username"]
    return render_template("savedplaylists.html", username=name)

# Code to bring up results from SQL based on HTML search, will include an add to playlist button

@app.route('/results', methods=["POST", "GET"])
def results():
    if request.method == "POST":
        start_year = request.form["decade"]
        end_year = int(start_year) + 10
        bechdel_rating = request.form["bechdel"]
        film_results = get_records_by_year_and_bech_rating(start_year, end_year, bechdel_rating)

        return render_template('results.html', film_results=film_results)

if __name__ == "__main__":
    app.run(debug=True)

