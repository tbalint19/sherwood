from django.test import TestCase
from App_Game.models import Team

class TeamTest(TestCase):

    def setUp(self):
        pass

    def test_iterator(self):
        team = Team(name="F.C. Barcelona", short_name="FC Barca", stadium="Camp Nou").save()
        data = {'id': team.id,'name': "F.C. Barcelona", 'short_name': "FC Barca", 'stadium': "Camp Nou"}
        self.asserEqual(data, dict(team))
