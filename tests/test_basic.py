import unittest
from flask_testing import TestCase
from app import app

class BasicTests(TestCase):

    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome to My Data Science Website', response.data)

    def test_about_us(self):
        response = self.client.get('/about-us')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'About Us', response.data)

    def test_intro_to_ds(self):
        response = self.client.get('/intro-to-ds')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Introduction to Data Science', response.data)

if __name__ == "__main__":
    unittest.main()
