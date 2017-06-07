from django.test import TestCase, tag
from _Test.database import populate_data, update_week
from _Test.user import TestUser
from App_Account.models import *
import json

@tag('story', 'archive_numbers')
class TestArchiveNumbers(TestCase):

    @classmethod
    def setUpTestData(cls):
        populate_data()
        update_week(1)

        user = TestUser()
        user.request_singnup(user.create_signup_data('Bela12', 'bela@bela.hu', '123456Ab', None))
        user.request_login(user.create_login_data('Bela12', '123456Ab'))

        cls.response = user.request_archive_numbers()

    def setUp(self):
        self.maxDiff = None

    def test_user_receives_respone(self):
        self.assertEqual(self.__class__.response.status_code, 200)

    def test_respone_contains_relevant_data(self):
        response_data = json.loads(self.__class__.response.content.decode('utf-8'))['archive_numbers']
        self.assertTrue(
            "won" in response_data and "lost" in response_data and
            "upcoming" in response_data and "live" in response_data and
            "private" in response_data and "trophies" in response_data)
