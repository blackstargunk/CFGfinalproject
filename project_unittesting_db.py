import unittest
import requests
import mysql.connector
from io import StringIO
from unittest.mock import patch
from db import (_connect_to_db, search_movies_database, get_records_by_year_and_bech_rating, login_to_website, register_an_account)

class TestingDbFunctions(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)

    def test_connect_to_db(self):
        #Testing that the database successfully connects with the _connect_to_db function
        connection = _connect_to_db("films")

        self.assertIsInstance(connection, mysql.connector.MySQLConnection)
        self.assertTrue(connection.is_connected())
        connection.close()

    def test_search_movies_database(self, mock_stdout):
        #Testing for successful search of movie with search function
        film_title = "Wild at Heart"

        search_movies_database(film_title)

        output = mock_stdout.getvalue().strip()

        self.assertIn(film_title, output)

    def test_get_records_by_year_and_bech_rating(self):
        #Testing the successful request for of Bechdel rating, bu inputted year
        start_year = 2000
        end_year = 2020
        bechdel_rating = "pass"

        result = get_records_by_year_and_bech_rating(start_year, end_year, bechdel_rating)

        self.assertIsInstance(result, list)
        self.assertGreater(len(result), 0)

    def test_login_to_website(self):
        # Testing correct/valid login details
        username = "test_user"
        password = "test_password"

        result = login_to_website(username, password)

        self.assertTrue(result)

        # Testing incorrect/invalid login details
        username = "invalid_user"
        password = "invalid_password"

        result = login_to_website(username, password)

        self.assertEqual(result, "Information provided does not match any accounts on the system")


    def test_register_an_account(self):
        #Testing for successful user account creation
        username = "new_user"
        password = "new_password"

        result = register_an_account(username, password)

        self.assertEqual(result, "Successful account creation")

if __name__ == '__main__':
    unittest.main()