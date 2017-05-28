from django.test import TestCase, tag
from _Test.util.user import TestUser
from _Test.util.data import TestData
from App_Profile.models import *
import json

@tag('story')
class TestStory(TestCase):

    @classmethod
    def setUpTestData(cls):
        player_1 = TestUser()

        login_data = player_1.create_login_data('Bela12', '123456Ab')
        cls.response_1 = player_1.request_login(login_data)

        login_data = player_1.create_login_data('bela@bela.hu', '123456Ab')
        cls.response_2 = player_1.request_login(login_data)

        signup_data = player_1.create_signup_data('Bela12', 'bela@bela.hu', '123456Ab', None)
        cls.response_3 = player_1.request_singnup(signup_data)

        cls.status_1 = {'users': len(Profile.objects.all()), 'invitations': len(Invitation.objects.all())}

        signup_data = player_1.create_signup_data('Bela12', 'bela@lajos.hu', '123456Ab', None)
        cls.response_4 = player_1.request_singnup(signup_data)

        signup_data = player_1.create_signup_data('Lajos12', 'bela@bela.hu', '123456Ab', None)
        cls.response_5 = player_1.request_singnup(signup_data)

        signup_data = player_1.create_signup_data('Bela12', 'bela@bela.hu', '123456Ab', None)
        cls.response_6 = player_1.request_singnup(signup_data)

        cls.status_2 = {'users': len(Profile.objects.all()), 'invitations': len(Invitation.objects.all())}

        signup_data = player_1.create_signup_data('Lajos12', 'lajos@lajos.hu', '123456Ab', 'Bela12')
        cls.response_7 = player_1.request_singnup(signup_data)

        cls.status_3 = {'users': len(Profile.objects.all()), 'invitations': len(Invitation.objects.all())}

        signup_data = player_1.create_signup_data('Kazmer12', 'kazmer@kazmer.hu', '123456Ab', 'Otto12')
        cls.response_8 = player_1.request_singnup(signup_data)

        cls.status_4 = {'users': len(Profile.objects.all()), 'invitations': len(Invitation.objects.all())}

        login_data = player_1.create_login_data('Bela12', '123456Ab')
        cls.response_9 = player_1.request_login(login_data)

        login_data = player_1.create_login_data('bela@bela.hu', '123456Ab')
        cls.response_10 = player_1.request_login(login_data)

        login_data = player_1.create_login_data('Bela12', '123456ACDEFg')
        cls.response_11 = player_1.request_login(login_data)

        login_data = player_1.create_login_data('bela@bela.hu', '123456ACDEFg')
        cls.response_12 = player_1.request_login(login_data)

        cls.response_13 = player_1.request_logout()

        profile = Profile.objects.get(user_obj__username='Bela12')
        cls.status_5 = profile.is_confirmed
        confirm_data = player_1.create_confirm_data('Bela12', profile.confirmation_code)
        cls.response_14 = player_1.request_email_confirm(confirm_data)
        profile = Profile.objects.get(user_obj__username='Bela12')
        cls.status_6 = profile.is_confirmed

        profile = Profile.objects.get(user_obj__username='Kazmer12')
        cls.status_7 = profile.is_confirmed
        confirm_data = player_1.create_confirm_data('Kazmer12', profile.confirmation_code + "somethingelse")
        cls.response_15 = player_1.request_email_confirm(confirm_data)
        profile = Profile.objects.get(user_obj__username='Kazmer12')
        cls.status_8 = profile.is_confirmed

    def setUp(self):
        self.maxDiff = None

    def test_user_tries_login_with_username_without_profile(self):
        response = self.__class__.response_1
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content.decode('utf-8')), {'is_successful': False})

    def test_user_tries_login_with_email_without_profile(self):
        response = self.__class__.response_2
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content.decode('utf-8')), {'is_successful': False})

    def test_user_signup_with_unoccupied_data(self):
        response = self.__class__.response_3
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content.decode('utf-8')), {'errors': []})

    def test_one_user_no_invitation(self):
        status = self.__class__.status_1
        self.assertEqual(status['users'], 1)
        self.assertEqual(status['invitations'], 0)

    def test_user_signup_with_occupied_username(self):
        response = self.__class__.response_4
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content.decode('utf-8')), {'errors': ["username"]})

    def test_user_signup_with_occupied_email(self):
        response = self.__class__.response_5
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content.decode('utf-8')), {'errors': ["email"]})

    def test_user_signup_with_occupied_username_and_email(self):
        response = self.__class__.response_6
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content.decode('utf-8')), {'errors': ["username", "email"]})

    def test_one_user_no_invitation_after_unsuccesful_attempts(self):
        status = self.__class__.status_2
        self.assertEqual(status['users'], 1)
        self.assertEqual(status['invitations'], 0)

    def test_user_signup_with_valid_inviter(self):
        response = self.__class__.response_7
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content.decode('utf-8')), {'errors': []})

    def test_two_user_one_invitation(self):
        status = self.__class__.status_3
        self.assertEqual(status['users'], 2)
        self.assertEqual(status['invitations'], 1)

    def test_user_signup_with_invalid_inviter(self):
        response = self.__class__.response_8
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content.decode('utf-8')), {'errors': []})

    def test_three_user_one_invitation(self):
        status = self.__class__.status_4
        self.assertEqual(status['users'], 3)
        self.assertEqual(status['invitations'], 1)

    def test_user_tries_login_with_valid_credentials_username(self):
        response = self.__class__.response_9
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content.decode('utf-8')), {'is_successful': True})

    def test_user_tries_login_with_valid_credentials_email(self):
        response = self.__class__.response_10
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content.decode('utf-8')), {'is_successful': True})

    def test_user_tries_login_with_username_and_wrong_password(self):
        response = self.__class__.response_11
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content.decode('utf-8')), {'is_successful': False})

    def test_user_tries_login_with_email_and_wrong_password(self):
        response = self.__class__.response_12
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content.decode('utf-8')), {'is_successful': False})

    def test_user_logout(self):
        response = self.__class__.response_13
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content.decode('utf-8')), {'is_successful': True})

    def test_user_is_not_confirmed(self):
        status = self.__class__.status_5
        self.assertFalse(status)

    def test_user_confirms_email(self):
        response = self.__class__.response_14
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content.decode('utf-8')), {'is_successful': True})

    def test_user_is_confirmed(self):
        status = self.__class__.status_6
        self.assertTrue(status)

    def test_other_user_is_not_confirmed(self):
        status = self.__class__.status_7
        self.assertFalse(status)

    def test_user_confirms_email_wrong_code(self):
        response = self.__class__.response_15
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content.decode('utf-8')), {'is_successful': False})

    def test_user_still_not_confirmed(self):
        status = self.__class__.status_8
        self.assertFalse(status)
