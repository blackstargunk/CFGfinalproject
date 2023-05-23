import requests
import mysql.connector


class DbConnectionError(Exception):
    pass


def _connect_to_db(films):
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Billybobmyspot1",
        database="Feminist_Films",
    )
    return connection


def search_movies_database(film_title):
    url = "https://moviesdatabase.p.rapidapi.com/titles/search/title/'{}'".format(film_title)

    querystring = {"exact": "false", "titleType": "movie"}

    headers = {
        "X-RapidAPI-Key": "40a78ce9ebmshbd91df11ae06b8fp149f9bjsnb829ec155bc9",
        "X-RapidAPI-Host": "moviesdatabase.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    code = response.json()
    movie_data = {}
    try:
        code['entries'] != 0
        try:
            movie_data['year'] = code['results'][0]['releaseDate']['year']
        except TypeError:
            movie_data['year'] = 'No further info available'
        else:
            movie_data['caption'] = code['results'][0]['primaryImage']['caption']['plainText']
            movie_data['url'] = code['results'][0]['primaryImage']['url']
    except:
        movie_data['year'] = 'No further info available'

    return movie_data


def get_records_by_year_and_bech_rating(start_year, end_year, bechdel_rating):
    db_connection = None
    results = []
    try:
        db_name = 'Feminist_Films'
        db_connection = _connect_to_db(db_name)

        cursor = db_connection.cursor()

        query = """SELECT *
                FROM Feminist_Films.films
                WHERE
                films.year
                BETWEEN '{}' AND '{}'
                HAVING rating = '{}';""".format(start_year, end_year, bechdel_rating)
        cursor.execute(query)
        result = cursor.fetchall()

        for row in result:
            # print(row)
            title = row[1]
            if '&' not in title:
                if title[-5] == ',':
                    realtitle = title[-4]
                    title = realtitle
                results.append(title)
        cursor.close()

    except Exception:
        raise DbConnectionError("Database connection unavailable.")
    finally:
        if db_connection:
            db_connection.close()

    return results


def login_to_website(username, password):
    db_connection = None

    try:
        db_name = 'Feminist_Films'
        db_connection = _connect_to_db(db_name)

        cursor = db_connection.cursor()

        account_query = """ SELECT * FROM Feminist_Films WHERE username = %s AND password = %s""".format(username, password)

        cursor.execute(account_query)
        search_results = cursor.fetchone()

        if account:
            session["loggedin"] = True
            session["id"] = account["id"]
            session["username"] = account["username"]
            # redirect to homepage
            return "Logged in Successfully!"
        else:
            output_message = "Incorrect username or password combination"

    except Exception:
        raise DbConnectionError("Database connection unavailable.")
    finally:
        if db_connection:
            db_connection.close()

    return search_results

def register_an_account():
    db_connection = None

    try:
        db_name = 'Feminist_Films'
        db_connection = _connect_to_db(db_name)

        cursor = db_connection.cursor()

        registration_query = """ SELECT * FROM users WHERE username = %s""".format(username)
        cursor.execute(registration_query)
        account_search = cursor.fetchone()
        output_message = ""
        if account_search:
            output_message = "This account already exists"
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            output_message = "Invalid email address entered"
        elif not re.match(r'[A-Za=z0-9]+', username):
            output_message = "Username must only contain letters and numbers"
        elif not username or not password or not email:
            output_message = "Please fill out the registration form"
        else:
            cursor.execute("INSERT INTO users VALUE (NULL, %s, %s, %s", (username, password, email))
            mysql.connection.commit()
            output_message = "You have successfully created an account"

    except Exception:
        raise DbConnectionError("Database connection unavailable.")
    finally:
        if db_connection:
            db_connection.close()

        return account_search






