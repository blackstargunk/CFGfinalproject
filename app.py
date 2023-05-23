from flask import Flask, render_template, request, redirect, url_for, session
from db import get_records_by_year_and_bech_rating
from db import login_to_website
from db import register_an_account

# after importing the modules, start writing the functions. When a function is wrapped in @app.route,
# it is the code for a webpage. All the html documents must be in the 'templates' folder to be rendered.
# all the CSS/images/styling must be in the 'static' folder to get picked up

app = Flask(__name__)


# homepage route
@app.route('/')
def homepage():
    return render_template('index.html')


# search bar route
@app.route('/search')
def search():
    return render_template('search_radio.html')


#Register for an account route
@app.route('/register', methods=["POST", "GET"])
def register():
   username = request.form.get("username")
   password = request.form.get("password")
   email = request.form.get("email")

   registration_results = register_an_account(username,password,email)

   return render_template("register.html", registration_results=registration_results)


# account login route
@app.route('/savedplaylists', methods=["POST", "GET"])
def playlists_login():
    username = request.form.get('username')
    password = request.form.get('password')

    account_results = login_to_website(username, password)
    return render_template("savedplaylists.html", account_results=account_results)

def logout():
    session.pop("loggedin", None)
    session.pop("id", None)
    session.pop("username", None)

    return redirect(url_for("login")) #this needs to match up with the HTML if there is a url_for login


# search results route
@app.route('/results', methods=["POST", "GET"])
def results():
    start_year = request.form.get('start_year')
    end_year = request.form.get('end_year')
    bechdel_rating = request.form.get('bechdel_rating')

    results = get_records_by_year_and_bech_rating(start_year, end_year, bechdel_rating)
    return render_template('results.html', results=results)

# about page route
@app.route('/about')
def about():
    pass

if __name__ == "__main__":
    app.run(port=8000, debug=True)

# to run the application via terminal and enter, in this order:
# FLASK_APP=app.py
# export FLASK_DEBUG=1
# flask run
