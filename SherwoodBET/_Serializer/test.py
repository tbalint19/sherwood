from django.test import TestCase
from _Serializer.serializer import Serializer as S
from App_Profile.models import Profile
from App_Game.models import Team, Match, Event, MatchEvent, Collection, MatchEventOfCollection, RaceTicket, UserTicket, Bet
from datetime import datetime

class SerializerTest(TestCase):

    def setUp(self):
        self.barca = Team(name="F.C. Barcelona", short_name="FC Barca", stadium="Camp Nou")
        self.rmadird = Team(name="Real Madrid C.F.", short_name="R Madrid", stadium="Bernabeu")
        deadline = datetime.strptime('Jun 1 2005  1:33PM', '%b %d %Y %I:%M%p')
        self.barca_real = Match(home_team_obj=self.barca, away_team_obj=self.rmadird, deadline=deadline)
        self.final_result = Event(name="Final result")
        self.barca_real_final_result = MatchEvent(match_obj=self.barca_real, event_obj=self.final_result)
        self.PD15_collection = Collection(number=171819, title="PD 15th round", intro="Play it!")
        self.barca_real_final_result_on_PD15_collection = MatchEventOfCollection(
            match_event_obj=self.barca_real_final_result, collection_obj=self.PD15_collection)
        self.PD15_collection_with_1_euro = RaceTicket(
            collection_obj=self.PD15_collection, is_professional=True, bet_amount=1)
        self.player = Profile.objects.create_profile("Kazmer12", "kaz@mer.hu", '123456Kazmer')
        self.user_ticket_of_kazmer = UserTicket(race_ticket_obj=self.PD15_collection_with_1_euro, user_obj=self.player)
        self.bet_on_barca_real_from_kazmer = Bet(
            match_event_obj=self.barca_real_final_result, user_ticket_obj=self.user_ticket_of_kazmer)

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
        serialized = S.serialize(self.PD15_collection)
        self.assertEquals(data, serialized)

    def test_serialize_match_event_of_collection(self):
        data = {'collection': '#171819: PD 15th round', 'id': None, 'match_event': 'FC Barca - R Madrid / Final result'}
        serialized = S.serialize(self.barca_real_final_result_on_PD15_collection)
        self.assertEquals(data, serialized)

    def test_serialize_race_ticket(self):
        data = {'collection': '#171819: PD 15th round', 'id': None,
            'is_professional': True, 'bet_amount': 1, 'number_of_competitors': 0}
        serialized = S.serialize(self.PD15_collection_with_1_euro)
        self.assertEquals(data, serialized)

    def test_serialize_user_ticket(self):
        data = {'finished': False, 'id': None, 'live': False, 'paid': False, 'payoff': None, 'points': 1,
            'race_ticket': '#171819: PD 15th round / 1', 'rank': None, 'user': 'Kazmer12'}
        serialized = S.serialize(self.user_ticket_of_kazmer)
        self.assertEquals(data, serialized)

    def test_serialize_user_ticket(self):
        data = {'finished': False, 'id': None, 'live': False, 'paid': False, 'payoff': None, 'points': 1,
            'race_ticket': '#171819: PD 15th round / 1', 'rank': None, 'user': 'Kazmer12'}
        serialized = S.serialize(self.user_ticket_of_kazmer)
        self.assertEquals(data, serialized)

    def test_serialize_bet(self):
        data = {'away': 0, 'draw': 0, 'home': 0, 'id': None, 'match_event': 'FC Barca - R Madrid / Final result',
            'result': 1, 'user_ticket': "Kazmer12's #171819: PD 15th round / 1"}
        serialized = S.serialize(self.bet_on_barca_real_from_kazmer)
        self.assertEquals(data, serialized)
