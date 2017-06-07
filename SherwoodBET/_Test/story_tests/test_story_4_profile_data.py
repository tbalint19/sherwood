from django.test import TestCase, tag
from _Test.user import TestUser
from App_Profile.models import *
import json

@tag('story', 'profile_data')
class TestProfileData(TestCase):

    @classmethod
    def setUpTestData(cls):
        user = TestUser()
        user.request_singnup(user.create_signup_data('Bela12', 'bela@bela.hu', '123456Ab', None))
        user.request_login(user.create_login_data('Bela12', '123456Ab'))

        cls.response = user.request_profile_data()

    def setUp(self):
        self.maxDiff = None

    def test_user_receives_respone(self):
        self.assertEqual(self.__class__.response.status_code, 200)

    def test_respone_contains_relevant_data(self):
        response_data = json.loads(self.__class__.response.content.decode('utf-8'))
        self.assertEqual(response_data['profile']['user'], "Bela12")
