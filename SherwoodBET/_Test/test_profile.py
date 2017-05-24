from django.test import TestCase, Client
from _Test.player import TestPlayer
from App_Profile.views import signup_user, login_user, logout_user

class TestProfile(TestCase):

    @classmethod
    def setUpTestData(cls):
        pass

    def setUp(self):
        pass

    def test_user_tries_login_with_username_without_profile(self):
        pass

    def test_user_tries_login_with_email_without_profile(self):
        pass

    def test_user_signup_with_unoccupied_data(self):
        pass

    def test_user_signup_with_occupied_username(self):
        pass

    def test_user_signup_with_occupied_email(self):
        pass

    def test_user_signup_with_occupied_username_and_email(self):
        pass

    def test_user_login_with_not_existing_username(self):
        pass

    def test_user_login_with_not_existing_email(self):
        pass

    def test_user_login_with_wrong_password(self):
        pass

    def test_user_login_with_valid_credentials(self):
        pass
