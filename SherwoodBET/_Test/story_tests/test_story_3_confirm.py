from django.test import TestCase, tag
from _Test.user import TestUser
from App_Profile.models import *
import json

@tag('story', 'confirm')
class TestConfirm(TestCase):

    @classmethod
    def setUpTestData(cls):
        user = TestUser()
        user.request_singnup(
            user.create_signup_data('Bela12', 'bela@bela.hu', '123456Ab', None))

        user.request_singnup(
            user.create_signup_data('Kazmer12', 'kazmer@kazmer.hu', '123456Ab', None))

        profile = Profile.objects.get(user_obj__username='Bela12')
        cls.user_is_confirmed_1 = profile.is_confirmed
        cls.correct_confirm_response = user.request_email_confirm(
            user.create_confirm_data('Bela12', profile.confirmation_code))
        cls.user_is_confirmed_2 = Profile.objects.get(user_obj__username='Bela12').is_confirmed

        profile = Profile.objects.get(user_obj__username='Kazmer12')
        cls.user_is_confirmed_3 = profile.is_confirmed
        cls.wrong_confirm_response = user.request_email_confirm(
            user.create_confirm_data('Kazmer12', profile.confirmation_code + "somethingelse"))
        cls.user_is_confirmed_4 = Profile.objects.get(user_obj__username='Kazmer12').is_confirmed

    def setUp(self):
        self.maxDiff = None

    def test_user_is_not_confirmed(self):
        user_is_confirmed = self.__class__.user_is_confirmed_1
        self.assertFalse(user_is_confirmed)

    def test_user_confirms_email(self):
        response = self.__class__.correct_confirm_response
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content.decode('utf-8')), {'is_successful': True})

    def test_user_is_confirmed(self):
        user_is_confirmed = self.__class__.user_is_confirmed_2
        self.assertTrue(user_is_confirmed)

    def test_other_user_is_not_confirmed(self):
        user_is_confirmed = self.__class__.user_is_confirmed_3
        self.assertFalse(user_is_confirmed)

    def test_user_confirms_email_wrong_code(self):
        response = self.__class__.wrong_confirm_response
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content.decode('utf-8')), {'is_successful': False})

    def test_user_still_not_confirmed(self):
        user_is_confirmed = self.__class__.user_is_confirmed_4
        self.assertFalse(user_is_confirmed)
