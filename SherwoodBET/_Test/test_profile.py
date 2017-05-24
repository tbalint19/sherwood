from django.test import TestCase
from _Test.player import TestPlayer
from django.contrib.auth.models import User
from App_Profile.models import Profile, Account
from App_Profile.views import signup_user, login_user, logout_user
import json

class TestProfile(TestCase):

    @classmethod
    def setUpTestData(cls):
        user_in_db = User.objects.create_user(
            username='DefaultInDB', email='Default@indb.hu', password='123456Ab')
        Profile(user_obj=user_in_db).save()
        Account(user_obj=user_in_db).save()

    def setUp(self):
        self.maxDiff = None

    def test_user_tries_login_with_username_without_profile(self):
        player = TestPlayer(created=False)
        response = player.request_login("username")
        self.assertEqual(json.loads(response.content.decode('utf-8')), {'is_successful': False})

    def test_user_tries_login_with_email_without_profile(self):
        player = TestPlayer(created=False)
        response = player.request_login("email")
        self.assertEqual(json.loads(response.content.decode('utf-8')), {'is_successful': False})

    def test_user_signup_with_unoccupied_data(self):
        player = TestPlayer(created=False)
        response = player.request_singnup()
        self.assertEqual(json.loads(response.content.decode('utf-8')), {'errors': []})

    def test_user_signup_with_occupied_username(self):
        player = TestPlayer(username="DefaultInDB", created=False)
        response = player.request_singnup()
        self.assertEqual(json.loads(response.content.decode('utf-8')), {'errors': ["username"]})

    def test_user_signup_with_occupied_email(self):
        player = TestPlayer(email="Default@indb.hu", created=False)
        response = player.request_singnup()
        self.assertEqual(json.loads(response.content.decode('utf-8')), {'errors': ["email"]})

    def test_user_signup_with_occupied_username_and_email(self):
        player = TestPlayer(username='DefaultInDB', email="Default@indb.hu", created=False)
        response = player.request_singnup()
        self.assertEqual(json.loads(response.content.decode('utf-8')), {'errors': ["username", "email"]})

    def test_user_login_with_not_existing_username(self):
        player = TestPlayer()
        player = TestPlayer(username="misspelled", logged_in=False, created=False)
        response = player.request_login("username")
        self.assertEqual(json.loads(response.content.decode('utf-8')), {'is_successful': False})

    def test_user_login_with_not_existing_email(self):
        player = TestPlayer()
        player = TestPlayer(email="mis@spelled.com", logged_in=False, created=False)
        response = player.request_login("email")
        self.assertEqual(json.loads(response.content.decode('utf-8')), {'is_successful': False})

    def test_user_login_with_wrong_password_but_good_username(self):
        player = TestPlayer()
        player = TestPlayer(password="misspelled", logged_in=False, created=False)
        response = player.request_login("username")
        self.assertEqual(json.loads(response.content.decode('utf-8')), {'is_successful': False})

    def test_user_login_with_wrong_password_but_good_email(self):
        player = TestPlayer()
        player = TestPlayer(password="misspelled", logged_in=False, created=False)
        response = player.request_login("email")
        self.assertEqual(json.loads(response.content.decode('utf-8')), {'is_successful': False})

    def test_user_login_with_valid_credentials_username(self):
        player = TestPlayer(logged_in=False)
        response = player.request_login("username")
        self.assertEqual(json.loads(response.content.decode('utf-8')), {'is_successful': True})

    def test_user_login_with_valid_credentials_email(self):
        player = TestPlayer(logged_in=False)
        response = player.request_login("email")
        self.assertEqual(json.loads(response.content.decode('utf-8')), {'is_successful': True})

    def test_user_logout(self):
        player = TestPlayer(logged_in=True)
        response = player.request_logout()
        self.assertEqual(json.loads(response.content.decode('utf-8')), {'is_successful': True})
