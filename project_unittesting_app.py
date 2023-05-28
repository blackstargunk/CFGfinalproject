import unittest
from flask import Flask
from flask_testing import TestCase
from unittest.mock import patch
from app import app


class AppTestCase(TestCase):
    def create_app(self):
        #CSRF protection disabled for the sake of testing for simplification purposes and ease of testing test cases.
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False 
        return app

    @patch('app.homepage')
    def test_homepage(self, mock_homepage):
        #Testing homepage function successfully called - tests the correct response occurs and the right template (index) is used, through mocking the function.
        mock_homepage.return_value = 'Mocked_homepage_response'
        response = self.client.get('/')
        self.assert200(response)
        self.assertTemplateUsed('index.html')
        mock_homepage.assert_called()

    @patch('app.search')
    def test_search(self, mock_search):
        #Testing search function successfully called - tests the correct response occurs and the right template (search_radio) is used, through mocking the function.
        mock_search.return_value = 'Mocked_search_response'
        response = self.client.get('/search')
        self.assert200(response)
        self.assertTemplateUsed('search_radio.html')
        mock_search.assert_called()

    @patch('app.playlists')
    def test_playlists(self, mock_playlists):
        #Testing playlists funtion successfully called - tests username is working as it should, also through mocking the function.
        mock_playlists.return_value = 'Mocked_playlists_response'
        response = self.client.post('/savedplaylists', data={'username': 'test_user'})
        self.assert200(response)
        self.assertTemplateUsed('savedplaylists.html')
        self.assertContext('username', 'test_user')
        mock_playlists.assert_called()

    @patch('app.results')
    def test_results(self, mock_results):
        #Testing results funtion successfully called - tests results is working as it should, also through mocking the function.
        mock_results.return_value = 'Mocked_results_response'
        response = self.client.post('/results', data={'start_year': '2000', 'end_year': '2020', 'bechdel_rating': 'pass'})
        self.assert200(response)
        self.assertTemplateUsed('results.html')
        self.assertContext('results')
        mock_results.assert_called()

    @patch('app.login')
    def test_login(self, mock_login):
        #Testing login funtion successfully called
        mock_login.return_value = 'Mocked_login_response'
        response = self.client.get('/login')
        self.assert200(response)
        self.assertTemplateUsed('login.html')
        mock_login.assert_called()


if __name__ == '__main__':
    unittest.main()
