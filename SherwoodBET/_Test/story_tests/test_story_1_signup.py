from django.test import TestCase, tag
from _Test.user import TestUser
from App_Profile.models import *
import json

@tag('story', 'signup')
class TestSignup(TestCase):

    @classmethod
    def setUpTestData(cls):
        user = TestUser()

        cls.correct_signup_response = user.request_singnup(
            user.create_signup_data('Bela12', 'bela@bela.hu', '123456Ab', None))

        cls.all_profiles_1 = list(Profile.objects.all())
        cls.all_invitations_1 = list(Invitation.objects.all())

        cls.existing_username_signup_response = user.request_singnup(
            user.create_signup_data('Bela12', 'bela@lajos.hu', '123456Ab', None))

        cls.existing_email_signup_response = user.request_singnup(
            user.create_signup_data('Lajos12', 'bela@bela.hu', '123456Ab', None))

        cls.existing_credentials_signup_response = user.request_singnup(
            user.create_signup_data('Bela12', 'bela@bela.hu', '123456Ab', None))

        cls.all_profiles_2 = list(Profile.objects.all())
        cls.all_invitations_2 = list(Invitation.objects.all())

        cls.existing_inviter_signup_response = user.request_singnup(
            user.create_signup_data('Lajos12', 'lajos@lajos.hu', '123456Ab', 'Bela12'))

        cls.all_profiles_3 = list(Profile.objects.all())
        cls.all_invitations_3 = list(Invitation.objects.all())

        cls.not_existing_inviter_signup_response = user.request_singnup(
            user.create_signup_data('Kazmer12', 'kazmer@kazmer.hu', '123456Ab', 'Otto12'))

        cls.all_profiles_4 = list(Profile.objects.all())
        cls.all_invitations_4 = list(Invitation.objects.all())

    def setUp(self):
        self.maxDiff = None

    def test_user_signup_with_unoccupied_data(self):
        response = self.__class__.correct_signup_response
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content.decode('utf-8')), {'errors': []})

    def test_one_user_no_invitation(self):
        profiles = self.__class__.all_profiles_1
        invitations = self.__class__.all_invitations_1
        self.assertEqual(len(profiles), 1)
        self.assertEqual(len(invitations), 0)

    def test_user_signup_with_occupied_username(self):
        response = self.__class__.existing_username_signup_response
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content.decode('utf-8')), {'errors': ["username"]})

    def test_user_signup_with_occupied_email(self):
        response = self.__class__.existing_email_signup_response
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content.decode('utf-8')), {'errors': ["email"]})

    def test_user_signup_with_occupied_username_and_email(self):
        response = self.__class__.existing_credentials_signup_response
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content.decode('utf-8')), {'errors': ["username", "email"]})

    def test_one_user_no_invitation_after_unsuccesful_attempts(self):
        profiles = self.__class__.all_profiles_2
        invitations = self.__class__.all_invitations_2
        self.assertEqual(len(profiles), 1)
        self.assertEqual(len(invitations), 0)

    def test_user_signup_with_valid_inviter(self):
        response = self.__class__.existing_inviter_signup_response
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content.decode('utf-8')), {'errors': []})

    def test_two_user_one_invitation(self):
        profiles = self.__class__.all_profiles_3
        invitations = self.__class__.all_invitations_3
        self.assertEqual(len(profiles), 2)
        self.assertEqual(len(invitations), 1)

    def test_user_signup_with_invalid_inviter(self):
        response = self.__class__.not_existing_inviter_signup_response
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content.decode('utf-8')), {'errors': []})

    def test_three_user_one_invitation(self):
        profiles = self.__class__.all_profiles_4
        invitations = self.__class__.all_invitations_4
        self.assertEqual(len(profiles), 3)
        self.assertEqual(len(invitations), 1)
