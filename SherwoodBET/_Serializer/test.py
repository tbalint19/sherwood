from django.test import TestCase
from _Serializer.serializer import Serializer as S
from App_Game.models import Team, Match, Event, MatchEvent, Collection
from datetime import datetime

class SerializerTest(TestCase):

    def setUp(self):
        self.barca = Team(name="F.C. Barcelona", short_name="FC Barca", stadium="Camp Nou")
        self.rmadird = Team(name="Real Madrid C.F.", short_name="R Madrid", stadium="Bernabeu")
        deadline = datetime.strptime('Jun 1 2005  1:33PM', '%b %d %Y %I:%M%p')
        self.barca_real = Match(home_team_obj=self.barca, away_team_obj=self.rmadird, deadline=deadline)
        self.final_result = Event(name="Final result")
        self.barca_real_final_result = MatchEvent(match_obj=self.barca_real, event_obj=self.final_result)
        self.collection = Collection(number=171819, title="PD 15th round", intro="Play it!")

    def test_serialize_team(self):
        data = {'name': "F.C. Barcelona", 'short_name': "FC Barca", 'stadium': "Camp Nou", 'id': self.barca.id}
        serialized = S.serialize(self.barca)
        self.assertEquals(data, serialized)

    def test_serialize_match(self):
        data = {'away_team': 'R Madrid', 'deadline': '2005-06-01T13:33:00', 'home_team': 'FC Barca', 'link': '',
            'id': self.barca_real.id, 'league': 'Friendly', 'live': False, 'over': False, 'round': '', 'upcoming': True}
        serialized = S.serialize(self.barca_real)
        self.assertEquals(data, serialized)

    def test_serialize_event(self):
        data = {'name': "Final result", 'id': self.final_result.id}
        serialized = S.serialize(self.final_result)
        self.assertEquals(data, serialized)

    def test_serialize_match_event(self):
        data = {'match': "FC Barca - R Madrid", 'event': "Final result",
            'id': self.barca_real_final_result.id, 'result': None, 'details': None}
        serialized = S.serialize(self.barca_real_final_result)
        self.assertEquals(data, serialized)

    def test_serialize_collection(self):
        data = {'deep_analysis': False, 'finished': False, 'hidden': True, 'intro': 'Play it!', 'live': False,
            'number': 171819, 'playable': False, 'title': 'PD 15th round'}
        serialized = S.serialize(self.collection)
        self.assertEquals(data, serialized)
