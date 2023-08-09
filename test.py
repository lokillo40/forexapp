import unittest
from flask import Flask
from app import app # import your Flask application

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True 

    def test_index_status_code(self):
        # sends HTTP GET request to the application
        # on the specified path
        result = self.app.get('/') 

        # assert the status code of the response
        self.assertEqual(result.status_code, 200)

    def test_index_data(self):
        result = self.app.post('/', data={'from_currency': 'USD', 'to_currency': 'EUR', 'amount': '100'})
        
        # assert the response data
        self.assertTrue(b'The conversion result is' in result.data)

    # add more tests for other functions


if __name__ == '__main__':
    unittest.main()
