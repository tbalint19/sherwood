from django.test import TestCase
from _Serializer.serializer import Serializer as S
from App_Game.models import Team, Match, Event
from datetime import datetime

class SerializerTest(TestCase):

    def test_serialize_team(self):
        team = Team(name="F.C. Barcelona", short_name="FC Barca", stadium="Camp Nou")
        team.save()
        data = {'name': "F.C. Barcelona", 'short_name': "FC Barca", 'stadium': "Camp Nou", 'id': team.id}
        serialized = S.serialize(team)
        self.assertEquals(data, serialized)

    def test_serialize_match(self):
        home_team = Team(name="F.C. Barcelona", short_name="FC Barca", stadium="Camp Nou")
        home_team.save()
        away_team = Team(name="Real Madrid C.F.", short_name="R Madrid", stadium="Bernabeu")
        away_team.save()
        deadline = datetime.strptime('Jun 1 2005  1:33PM', '%b %d %Y %I:%M%p')
        match = Match(home_team_obj=home_team, away_team_obj=away_team, deadline=deadline)
        match.save()
        data = {'away_team': 'R Madrid', 'deadline': '2005-06-01T13:33:00', 'home_team': 'FC Barca', 'id': match.id,
            'league': 'Friendly', 'link': '', 'live': False, 'over': False, 'round': '', 'upcoming': True}
        serialized = S.serialize(match)
        self.assertEquals(data, serialized)

    def test_serialize_event(self):
        event = Event(name="Final result")
        event.save()
        data = {'name': "Final result", 'id': event.id}
        serialized = S.serialize(event)
        self.assertEquals(data, serialized)
