import unittest
from unittest.mock import patch
from db import (_connect_to_db, search_movies_database, get_records_by_year_and_bech_rating, login_to_website, register_an_account)

class TestingDbFunctions(unittest.TestCase):

    def test_connect_to_db(self):
       # Testing that the database successfully connects with the _connect_to_db function
        connection = _connect_to_db('films')
        self.assertIsNotNone(connection)
        connection.close()

    @patch('requests.get')
    def test_search_movies_database(self, mock_get):
        # Test the movie database search functionality
        mock_response = {
            'results': [
                {
                    'primaryImage': {
                        'caption': {
                            'plainText': 'Movie Title'
                        }
                    }
                }
            ]
        }
        mock_get.return_value.json.return_value = mock_response

        film_title = 'Movie Title'
        search_movies_database(film_title)

    def test_get_records_by_year_and_bech_rating(self):
        # Testing for successful search of movie with search function
        start_year = 2010
        end_year = 2020
        bechdel_rating = 'pass'
        results = get_records_by_year_and_bech_rating(start_year, end_year, bechdel_rating)
        self.assertEqual(len(results), 0)

    def test_login_to_website(self):
       # Testing correct/valid login details
        username = 'testuser'
        password = 'testpassword'
        result = login_to_website(username, password)
        self.assertEqual(result, True)

    def test_register_an_account(self):
        # Testing for successful user account creation
        username = 'newuser'
        password = 'newpassword'
        result = register_an_account(username, password)
        self.assertEqual(result, "You have successfully created an account")

if __name__ == '__main__':
    unittest.main()
