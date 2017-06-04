from django.test import TestCase, tag
from _Test.user import TestUser
from App_Profile.models import *
import json

@tag('story', 'login')
class TestLogin(TestCase):

    @classmethod
    def setUpTestData(cls):
        user = TestUser()

        cls.no_username_login_response = user.request_login(
            user.create_login_data('Bela12', '123456Ab'))

        cls.no_email_login_response = user.request_login(
            user.create_login_data('bela@bela.hu', '123456Ab'))

        user.request_singnup(
            user.create_signup_data('Bela12', 'bela@bela.hu', '123456Ab', None))

        cls.correct_username_login_response = user.request_login(
            user.create_login_data('Bela12', '123456Ab'))

        cls.correct_logout_response = user.request_logout()

        cls.wrong_password_username_login_response = user.request_login(
            user.create_login_data('Bela12', '123456ACDEFg'))

        cls.wrong_password_email_login_response = user.request_login(
            user.create_login_data('bela@bela.hu', '123456ACDEFg'))

        cls.correct_email_login_response = user.request_login(
            user.create_login_data('bela@bela.hu', '123456Ab'))

    def setUp(self):
        self.maxDiff = None

    def test_user_tries_login_with_username_without_profile(self):
        response = self.__class__.no_username_login_response
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content.decode('utf-8')), {'is_successful': False})

    def test_user_tries_login_with_email_without_profile(self):
        response = self.__class__.no_email_login_response
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content.decode('utf-8')), {'is_successful': False})

    def test_user_tries_login_with_valid_credentials_username(self):
        response = self.__class__.correct_username_login_response
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content.decode('utf-8')), {'is_successful': True})

    def test_user_logout(self):
        response = self.__class__.correct_logout_response
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content.decode('utf-8')), {'is_successful': True})

    def test_user_tries_login_with_username_and_wrong_password(self):
        response = self.__class__.wrong_password_username_login_response
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content.decode('utf-8')), {'is_successful': False})

    def test_user_tries_login_with_email_and_wrong_password(self):
        response = self.__class__.wrong_password_email_login_response
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content.decode('utf-8')), {'is_successful': False})

    def test_user_tries_login_with_valid_credentials_email(self):
        response = self.__class__.correct_email_login_response
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content.decode('utf-8')), {'is_successful': True})
