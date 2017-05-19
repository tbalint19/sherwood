from django.test import TestCase
from App_Game.models import Team

class TeamTest(TestCase):

    def setUp(self):
        pass

    def test_iterator(self):
        Team(name="F.C. Barcelona", short_name="FC Barca", stadium="Camp Nou").save()
        team = Team.objects.get(short_name="FC Barca")
        data = {'name': "F.C. Barcelona", 'short_name': "FC Barca", 'stadium': "Camp Nou", 'id': 1}
        self.assertEquals(data, dict(team))
