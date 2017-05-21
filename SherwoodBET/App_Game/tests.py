from django.test import TestCase, RequestFactory
from _Serializer.serializer import Serializer as S
from django.contrib.auth.models import AnonymousUser, User
from App_Profile.models import Profile
from App_Game.views import get_offer
from App_Game.factories import TeamFactory, MatchFactory, EventFactory, MatchEventFactory, CollectionFactory, RaceTicketFactory
from App_Game.models import Team, Event, Match, MatchEvent, Collection
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

class OfferTest(TestCase):

    def setUp(self):
        self.user = Profile.objects.create_profile(username="Kazmer12", email="kaz@mer.hu", password="123456Ab")
        self.request_factory = RequestFactory()
        self.team_factory = TeamFactory()
        self.match_factory = MatchFactory()
        self.event_factory = EventFactory()
        self.match_event_factory = MatchEventFactory()
        self.collection_factory = CollectionFactory()
        self.race_ticket_factory = RaceTicketFactory()
        # self.user_ticket_factory = UserTicketFactory()
        # self.bet_factory = BetFactory()

    # def test_get_offer_public(self):
    #     teams = self.team_factory.create_teams(14)
    #     events = self.event_factory.create_events()
    #     matches = self.match_factory.create_matches(teams)
    #     match_events = self.match_event_factory.create_match_events(matches, events)
    #     collections = self.collection_factory.create_collections(matches, events)
    #     race_tickets = self.race_ticket_factory.create_race_tickets(collections)
    #     request = self.request_factory.get('/game/api/get_offer')
    #     request.user = AnonymousUser()
    #     response = get_offer(request)
    #     blueprint = {"matches_offer": [], "deep_analysis_offer": [], "played_race_tickets": []}
    #     self.assertEqual({}, json.loads(response.content.decode('utf-8')))
