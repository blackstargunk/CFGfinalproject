import requests
from pprint import pprint
import mysql.connector



class DbConnectionError(Exception):
    pass


def _connect_to_db(films):
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Billybobmyspot1",
        database="films",
        auth_plugin="mysql_native_password"
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
    try:
        db_name = 'films'

        db_connection = _connect_to_db(db_name)

        cursor = db_connection.cursor()

        query = """SELECT *
                FROM film
                WHERE
                year
                BETWEEN '{}' AND '{}'
                HAVING rating = '{}';""".format(start_year, end_year, bechdel_rating)

        cursor.execute(query)
        result = cursor.fetchall()

        for row in result:
            print(row)
            title = row[1]
            search_movies_database(title)
        cursor.close()

    except Exception:
        raise DbConnectionError("Database connection unavailable.")
    finally:
        if db_connection:
            db_connection.close()

