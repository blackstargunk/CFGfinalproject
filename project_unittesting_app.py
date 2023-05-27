import unittest
from flask import Flask
from flask_testing import TestCase
from app import app, homepage, search, playlists, results, login


class AppTestCase(TestCase):
    def create_app(self):
        app.config['Testing_successful'] = True
        return app

    def test_homepage(self):
        response = self.client.get('/')
        self.assert200(response)
        self.assertTemplateUsed('index.html')

    def test_search(self):
        response = self.client.get('/search')
        self.assert200(response)
        self.assertTemplateUsed('search_radio.html')

    def test_playlists(self):
        response = self.client.post('/savedplaylists', data={'username': 'test_user'})
        self.assert200(response)
        self.assertTemplateUsed('savedplaylists.html')
        self.assertContext('username', 'test_user')

    def test_results(self):
        response = self.client.post('/results', data={'start_year': '2000', 'end_year': '2020', 'bechdel_rating': 'pass'})
        self.assert200(response)
        self.assertTemplateUsed('results.html')
        self.assertContext('results')

    def test_login(self):
        response = self.client.get('/login')
        self.assert200(response)
        self.assertTemplateUsed('login.html')


if __name__ == '__main__':
    unittest.main()
