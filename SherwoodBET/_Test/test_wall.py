from django.test import TestCase, Client
from _Test.player import TestPlayer
from App_Profile.views import *

class TestProfile(TestCase):

    @classmethod
    def setUpTestData(cls):
        pass

    def setUp(self):
        pass

    def test_user_requests_stories_without_filter(self):
        pass

    def test_user_requests_stories_about_announcements(self):
        pass

    def test_user_requests_stories_about_matches(self):
        pass

    def test_user_requests_stories_about_friends(self):
        pass

    def test_user_requests_own_stories(self):
        pass

    def test_user_shares_story(self):
        pass

    def test_user_comments_on_story(self):
        pass

    def test_user_likes_story(self):
        pass
