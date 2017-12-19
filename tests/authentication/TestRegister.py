""" API testing """

from tests.TestApp import BaseTestCase
import json


class FlaskTestCase(BaseTestCase):
    pass

    # def test_should_conflict(self):
    #     """
    #     Expect an error response on database conflict
    #     """
    #     with self.app.test_client() as client:
    #         self.assertEqual(
    #             client.post(
    #                 '/api/register',
    #                 headers={'Content-Type': 'application/json'},
    #                 data=json.dumps({'email': 'jimfilippou@hotmail.gr', 'pass': '12345'})
    #             ).status_code,
    #             409
    #         )


    # def test_should_return_payload_error(self):
    #     """
    #     Expect an error response when payload headers are incorrect
    #     """
    #     with self.app.test_client() as client:
    #         response = client.post(
    #             '/api/register',
    #             headers={'Content-Type': 'application/power puff girls'},
    #             data=json.dumps({'email': 'jimfilippou@hotmail.gr', 'pass': '12345'})
    #         )
    #         self.assert400(response)
    #         self.assertEqual(response.json["message"], "payload_error")


    # def test_should_tell_me_that_keyerror_was_raised(self):
    #     """
    #     Expect an error response when i don't send the right json body.
    #     """
    #     with self.app.test_client() as client:
    #         response = client.post(
    #             '/api/register',
    #             headers={'Content-Type': 'application/json'},
    #             data=json.dumps({
    #                 'email': 'jimfilippou@hotmail.gr',
    #                 'passw': '12345'
    #             })
    #         )
    #         self.assert400(response)
    #         self.assertEqual(response.json["message"], "key_error")


    # def test_should_register_successfully(self):
    #     """
    #     Expect to get a success response on a valid user registration, also get a token.
    #     """
    #     with self.app.test_client() as client:
    #         response = client.post(
    #             '/api/register',
    #             headers={'Content-Type': 'application/json'},
    #             data=json.dumps({'email': 'jimfilippou8@gmail.com', 'pass': '12345'})
    #         )
    #         self.assertEqual(response.status_code, 201)
    #         self.assertGreater(len(response.json["token"]), 1)
