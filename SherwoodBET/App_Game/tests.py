from django.test import TestCase, RequestFactory
from _Serializer.serializer import Serializer as S
from django.contrib.auth.models import AnonymousUser, User
from App_Profile.models import Profile
from App_Game.views import get_offer, get_ticket
from App_Game.factories import (
    TeamFactory, MatchFactory, EventFactory, MatchEventFactory, CollectionFactory, RaceTicketFactory)
from App_Game.models import (
    Team, Event, Match, MatchEvent, Collection, RaceTicket, UserTicket, Bet)
import json

class FactoryTest(TestCase):

    def test_team_factory(self):
        TeamFactory().create_teams(14)
        team_names = set([str(team) for team in Team.objects.all()])
        self.assertEqual(len(team_names), 14)

    def test_event_factory(self):
        EventFactory().create_events()
        event_names = set([str(event) for event in Event.objects.all()])
        self.assertEqual(len(event_names), 7)

    def test_match_factory(self):
        teams = TeamFactory().create_teams(20)
        MatchFactory().create_matches(teams)
        matches = set([str(match) for match in Match.objects.all()])
        self.assertEqual(len(matches), 10)

    def test_match_event_factory(self):
        teams = TeamFactory().create_teams(20)
        events = EventFactory().create_events()
        matches = MatchFactory().create_matches(teams)
        MatchEventFactory().create_match_events(matches, events)
        match_events = set([str(match_event) for match_event in MatchEvent.objects.all()])
        self.assertEqual(len(match_events), 70)

    def test_collection_factory_one_match(self):
        teams = TeamFactory().create_teams(14)
        events = EventFactory().create_events()
        matches = MatchFactory().create_matches(teams)
        MatchEventFactory().create_match_events(matches, events)
        CollectionFactory().create_match_collections(matches, events)
        self.assertEqual(len(Collection.objects.all()), 7)

    def test_collection_factory_many_matches(self):
        teams = TeamFactory().create_teams(28)
        events = EventFactory().create_events()
        matches = MatchFactory().create_matches(teams)
        MatchEventFactory().create_match_events(matches, events)
        CollectionFactory().create_matches_collections()
        self.assertEqual(len(Collection.objects.all()), 2)

    def test_race_ticket_factory(self):
        teams = TeamFactory().create_teams(28)
        events = EventFactory().create_events()
        matches = MatchFactory().create_matches(teams)
        MatchEventFactory().create_match_events(matches, events)
        matches_collections = CollectionFactory().create_matches_collections()
        match_collections = CollectionFactory().create_match_collections(matches, events)
        RaceTicketFactory().create_race_tickets(match_collections + matches_collections)
        self.assertEqual(len(Collection.objects.all()), 16)

class OfferTestSunnyDayNoUser(TestCase):

    @classmethod
    def setUpTestData(cls):
        teams = TeamFactory().create_teams(28)
        events = EventFactory().create_events()
        matches = MatchFactory().create_matches(teams)
        MatchEventFactory().create_match_events(matches, events)
        cls.matches_collections = CollectionFactory().create_matches_collections()
        cls.match_collections = CollectionFactory().create_match_collections(matches, events)
        RaceTicketFactory().create_race_tickets(cls.match_collections + cls.matches_collections)
        cls.request = RequestFactory().get('/game/api/get_offer')
        cls.request.user = AnonymousUser()

    def setUp(self):
        self.maxDiff = None

    def test_three_fields_present(self):
        response = get_offer(self.__class__.request)
        response_data = json.loads(response.content.decode('utf-8'))
        self.assertTrue(
            "matches_offer" in response_data and
            "deep_analysis_offer" in response_data and
            "played_race_tickets" in response_data)

    def test_match_offer_contains_2_matches_collections_for_14_matches(self):
        response = get_offer(self.__class__.request)
        response_data = json.loads(response.content.decode('utf-8'))
        self.assertEqual(len(response_data["matches_offer"]), 2)

    def test_matches_offer_contains_14_match_collections_for_14_matches(self):
        response = get_offer(self.__class__.request)
        response_data = json.loads(response.content.decode('utf-8'))
        self.assertEqual(len(response_data["deep_analysis_offer"]), 14)

    def test_no_played_user_ticket_for_anonymususer(self):
        response = get_offer(self.__class__.request)
        response_data = json.loads(response.content.decode('utf-8'))
        self.assertEqual(len(response_data["played_race_tickets"]), 0)

    def test_matches_collections_contains_three_fields(self):
        response = get_offer(self.__class__.request)
        response_data = json.loads(response.content.decode('utf-8'))
        collection = response_data["matches_offer"][0]
        self.assertTrue(
            "race_tickets" in collection and
            "collection" in collection and
            "match_events" in collection)

    def test_match_collections_contains_three_fields(self):
        response = get_offer(self.__class__.request)
        response_data = json.loads(response.content.decode('utf-8'))
        collection = response_data["deep_analysis_offer"][0]
        self.assertTrue(
            "race_tickets" in collection and
            "collection" in collection and
            "match_events" in collection)

    def test_matches_collections_race_tickets_contains_6_different(self):
        response = get_offer(self.__class__.request)
        response_data = json.loads(response.content.decode('utf-8'))
        race_tickets = response_data["deep_analysis_offer"][0]["race_tickets"]
        race_ticket_data = [json.dumps(race_ticket, sort_keys=True) for race_ticket in race_tickets]
        self.assertEqual(len(set(race_ticket_data)), 6)

    def test_match_collections_race_tickets_contains_6_different(self):
        response = get_offer(self.__class__.request)
        response_data = json.loads(response.content.decode('utf-8'))
        race_tickets = response_data["matches_offer"][0]["race_tickets"]
        race_ticket_data = [json.dumps(race_ticket, sort_keys=True) for race_ticket in race_tickets]
        self.assertEqual(len(set(race_ticket_data)), 6)

    def test_match_collections_match_events_contains_7_different_match_event(self):
        response = get_offer(self.__class__.request)
        response_data = json.loads(response.content.decode('utf-8'))
        match_events = response_data["matches_offer"][0]["match_events"]
        match_events_data = [json.dumps(match_event, sort_keys=True) for match_event in match_events]
        self.assertEqual(len(set(match_events_data)), 7)

    def test_matches_collections_match_events_contains_7_different_match_events(self):
        response = get_offer(self.__class__.request)
        response_data = json.loads(response.content.decode('utf-8'))
        match_events = response_data["deep_analysis_offer"][0]["match_events"]
        match_events_data = [json.dumps(match_event, sort_keys=True) for match_event in match_events]
        self.assertEqual(len(set(match_events_data)), 7)

    def test_matches_offer_does_not_contain_not_playable(self):
        self.__class__.matches_collections[0].playable = False
        self.__class__.matches_collections[0].save()
        response = get_offer(self.__class__.request)
        response_data = json.loads(response.content.decode('utf-8'))
        self.assertEqual(len(response_data["matches_offer"]), 1)

    def test_match_offer_does_not_contain_not_playable(self):
        self.__class__.match_collections[0].playable = False
        self.__class__.match_collections[0].save()
        response = get_offer(self.__class__.request)
        response_data = json.loads(response.content.decode('utf-8'))
        self.assertEqual(len(response_data["deep_analysis_offer"]), 13)

class TicketTestSunnyDay(TestCase):

    @classmethod
    def setUpTestData(cls):
        teams = TeamFactory().create_teams(28)
        events = EventFactory().create_events()
        matches = MatchFactory().create_matches(teams)
        MatchEventFactory().create_match_events(matches, events)
        cls.matches_collections = CollectionFactory().create_matches_collections()
        cls.match_collections = CollectionFactory().create_match_collections(matches, events)
        RaceTicketFactory().create_race_tickets(cls.match_collections + cls.matches_collections)
        cls.race_ticket_id = RaceTicket.objects.filter(is_professional=False)[0].id
        cls.request = RequestFactory().get('/game/api/get_ticket?race_ticket_id=' + str(cls.race_ticket_id))
        cls.request.user = Profile.objects.create_profile("belane", "bela@ne.hu", '123456Ab')

    def setUp(self):
        self.maxDiff = None

    def test_response_given(self):
        response = get_ticket(self.__class__.request)
        response_data = json.loads(response.content.decode('utf-8'))
        self.assertEqual(response.status_code, 200)

    def test_contains_two_fields(self):
        response = get_ticket(self.__class__.request)
        response_data = json.loads(response.content.decode('utf-8'))
        self.assertTrue("user_ticket" in response_data and "related_bets" in response_data)

    def test_user_ticket_created(self):
        response = get_ticket(self.__class__.request)
        user_tickets = UserTicket.objects.filter(user_obj=self.__class__.request.user)
        self.assertTrue(len(user_tickets) == 1)
        self.assertTrue(user_tickets[0].race_ticket_obj.id == self.__class__.race_ticket_id)
