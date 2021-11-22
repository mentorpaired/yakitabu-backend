import os
import json

from unittest import TestCase
from dotenv import load_dotenv

from src import app, create_app
from src.user import decode_token, login, get_user_info, get_last_unreturned_book
from src.constants.http_status_codes import HTTP_200_OK, HTTP_404_NOT_FOUND, HTTP_405_METHOD_NOT_ALLOWED,HTTP_400_BAD_REQUEST


load_dotenv()

class TestUser(TestCase):

    
    def test_token_decode(self):
        """
        Test for decoding token and extracting user information.
        """

        token = {
            'id_token': os.environ.get("TEST_TOKEN")
                   }
        decoded_token = decode_token(token['id_token'])

        self.assertEqual(decoded_token['email'], os.environ.get("EMAIL"))
        self.assertEqual(decoded_token['given_name'], 'Yakitabu')
        self.assertEqual(decoded_token['family_name'], 'Project')

    def test_valid_login(self):
        """
        Test case covering Valid Login
        """
        token = {
            'id_token': os.environ.get("TEST_TOKEN")
                   }
        flask_app = create_app()
        

        with flask_app.test_client() as test_client:
            response = test_client.post('http://localhost:5000/api/v1/user/login/google',
                                        data=json.dumps(token),
                                        content_type='application/json',
                                        )
            assert response.status_code == HTTP_200_OK
            

    def test_invalid_login(self):
        """
        Test case covering Bad Request
        """
        token = {'id_token': "5om3InvalidTokeN"}
        flask_app = create_app()
        

        with flask_app.test_client() as test_client:
            response = test_client.post('http://localhost:5000/api/v1/user/login/google',
                                        data=json.dumps(token),
                                        content_type='application/json',
                                        )
            assert response.status_code == HTTP_400_BAD_REQUEST
       
    def test_login_get(self):
        """
        Test case covering unsupported METHOD: POST
        """

        flask_app = create_app()

        with flask_app.test_client() as test_client:
            response = test_client.get('http://localhost:5000/api/v1/user/login/google')

            assert response.status_code == HTTP_405_METHOD_NOT_ALLOWED
            
            
    def test_login_put(self):
        """
        Test case covering unsupported METHOD: PUT
        """

        flask_app = create_app()

        with flask_app.test_client() as test_client:
            response = test_client.get('http://localhost:5000/api/v1/user/login/google')

            assert response.status_code == HTTP_405_METHOD_NOT_ALLOWED


if __name__ == '__main__':
    unittest.main()