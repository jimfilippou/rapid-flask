""" API testing """

import os
from base64 import b64encode
from tests.TestApp import BaseTestCase


class FlaskTestCase(BaseTestCase):

    def test_should_get_token(self):
        """
        Expect a token from a valid sign in
        """
        with self.app.test_client() as client:
            response = client.post(
                '/v0/login',
                headers={
                    'Authorization': 'Basic %s' % b64encode("rickgrimmes@amc.com:michowned69"),
                    'Content-Type': 'application/json'
                }
            )
            self.assertEqual(response.status_code, 200)
            # Works only on windows
            with open("%s\\tests\\store\\token.dat" % os.getcwd(), 'w') as token_file:
                token_file.write(response.json["token"])

    def test_should_not_find_user(self):
        """
        Expect an error response on invalid login
        """
        with self.app.test_client() as client:
            self.assert404(
                client.post(
                    '/v0/login',
                    headers={
                        'Authorization': 'Basic %s' % b64encode("buckyroberts@thenewboston.com:12345"),
                        'Content-Type': 'application/json'
                    }
                )
            )

    def test_should_not_deliver_auth(self):
        """
        Expect an error response on null Authorization or a typo
        """
        with self.app.test_client() as client:
            self.assert400(
                client.post(
                    '/v0/login',
                    headers={
                        'AuthorizaSion': 'Basic %s' % "Not encoded string",
                        'Content-Type': 'application/power puff girls'
                    }
                )
            )

    def test_password_should_be_wrong(self):
        """
        Expect an error response on invalid password login
        """
        with self.app.test_client() as client:
            self.assert401(
                client.post(
                    '/v0/login',
                    headers={
                        'Authorization': 'Basic %s' % b64encode("rickgrimmes@amc.com:123456"),
                        'Content-Type': 'application/json'
                    }
                )
            )
