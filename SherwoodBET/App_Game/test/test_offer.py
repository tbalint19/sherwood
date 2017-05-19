from django.test import TestCase, RequestFactory
from _Serializer.serializer import Serializer as S
from django.contrib.auth.models import AnonymousUser, User
from App_Profile.models import Profile
from App_Game.models import Collection
from App_Game.views import get_offer
import json

class SerializerTest(TestCase):

    def setUp(self):
        self.user = Profile.objects.create_profile(username="Kazmer12", email="kaz@mer.hu", password="123456Ab")
        self.factory = RequestFactory()

    def test_get_offer_public(self):
        request = self.factory.get('/game/api/get_offer')
        request.user = AnonymousUser()
        response = get_offer(request)
        blueprint = {"matches_offer": [], "deep_analysis_offer": [], "played_race_tickets": []}
        self.assertEqual(blueprint, json.loads(response.content.decode('utf-8')))
