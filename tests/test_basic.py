""" Basic testing """

import unittest

from tests.base import BaseTestCase

class FlaskTestCase(BaseTestCase):

    """ Make sure everything is set up, i don't really enjoy doing this but eh... """

    # Ensure that Flask was set up correctly
    def test_index(self):
        response = self.client.get('/auth/login', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # Ensure that welcome page loads
    def test_welcome_route_works_as_expected(self):
        response = self.client.get('/', follow_redirects=True)
        self.assertIn(b'Welcome to flask', response.data)


if __name__ == '__main__':
    unittest.main()
