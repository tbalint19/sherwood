from App_Game.models import Team, Event, Match, MatchEvent, Collection, MatchEventOfCollection, RaceTicket
from django.test import TestCase, tag
from _Test.database import populate_data, update_week

@tag('database')
class TestDatabase(TestCase):

    @classmethod
    def setUpTestData(cls):
        populate_data()

    def setUp(self):
        self.maxDiff = None

    def test_teams(self):
        teams = [obj for obj in Team.objects.all()]
        names = [team.short_name for team in teams]
        self.assertEqual(len(teams), 58)
        self.assertEqual(len(teams), len(set(names)))

    def test_events(self):
        events = [obj for obj in Event.objects.all()]
        names = [event.name for event in events]
        self.assertEqual(len(events), 8)
        self.assertEqual(len(events), len(set(names)))

    def test_matches(self):
        matches = [obj for obj in Match.objects.all()]
        names = [match.home_team_obj.short_name + "-" + match.away_team_obj.short_name for match in matches]
        opp = [match.away_team_obj.short_name + "-" + match.home_team_obj.short_name for match in matches]
        self.assertEqual(len(matches), 63)
        self.assertEqual(len(matches), len(set(names)))
        self.assertEqual(len(set(names + opp)), 126)

    def test_match_events(self):
        match_events = [obj for obj in MatchEvent.objects.all()]
        self.assertEqual(len(match_events), 117)

    def test_collections(self):
        collections = [obj for obj in Collection.objects.all()]
        hidden = Collection.objects.filter(status=Collection.HIDDEN)
        self.assertEqual(len(collections), 18)
        self.assertEqual(len(hidden), 18)

    def test_match_events_of_collections(self):
        match_event_of_collections = [obj for obj in MatchEventOfCollection.objects.all()]
        self.assertEqual(len(match_event_of_collections), 126)

    def test_race_tickets(self):
        race_tickets = [obj for obj in RaceTicket.objects.all()]
        self.assertEqual(len(race_tickets), 108)

    def test_first_week(self):
        update_week(1)
        hidden = Collection.objects.filter(status=Collection.HIDDEN)
        playable = Collection.objects.filter(status=Collection.PLAYABLE)
        self.assertEqual(len(hidden), 12)
        self.assertEqual(len(playable), 6)

    def test_second_week(self):
        update_week(1)
        update_week(2)
        hidden = Collection.objects.filter(status=Collection.HIDDEN)
        playable = Collection.objects.filter(status=Collection.PLAYABLE)
        self.assertEqual(len(hidden), 12)
        self.assertEqual(len(playable), 6)

    def test_third_week(self):
        update_week(1)
        update_week(2)
        update_week(3)
        hidden = Collection.objects.filter(status=Collection.HIDDEN)
        playable = Collection.objects.filter(status=Collection.PLAYABLE)
        self.assertEqual(len(hidden), 12)
        self.assertEqual(len(playable), 6)
