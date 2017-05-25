# from django.test import TestCase, Client
# from _Test.player import TestPlayer
# from _Test.factory import *
# from App_Game.views import get_offer, get_ticket, place_bet
# import json
#
# class TestOffer(TestCase):
#
#     @classmethod
#     def setUpTestData(cls):
#         teams = TeamFactory().create_teams(28)
#         events = EventFactory().create_events()
#         matches = MatchFactory().create_matches(teams)
#         MatchEventFactory().create_match_events(matches, events)
#         matches_collections = CollectionFactory().create_matches_collections()
#         match_collections = CollectionFactory().create_match_collections(matches, events)
#         RaceTicketFactory().create_race_tickets(match_collections + matches_collections)
#         player = TestPlayer()
#         response = player.request_offer()
#         cls.response_data = json.loads(response.content.decode('utf-8'))
#
#     def setUp(self):
#         self.maxDiff = None
#
#     def test_data_set_up(self):
#         self.assertEqual(len(Team.objects.all()), 28)
#         self.assertEqual(len(Match.objects.all()), 14)
#         self.assertEqual(len(Event.objects.all()), 7)
#         self.assertEqual(len(MatchEvent.objects.all()), 98)
#         self.assertEqual(len(Collection.objects.filter(deep_analysis=True)), 14)
#         self.assertEqual(len(Collection.objects.filter(deep_analysis=False)), 2)
#         self.assertEqual(len(RaceTicket.objects.all()), 96)
#
#     def test_user_checks_offer_without_played_tickets(self):
#         player = TestPlayer()
#         response = player.request_offer()
#         response_data = json.loads(response.content.decode('utf-8'))
#
#         # matches offer
#         self.assertTrue(type(response_data["matches_offer"]) is list)
#         self.assertEqual(len(response_data["matches_offer"]), 2)
#         self.assertTrue(type(response_data["matches_offer"][0]["collection"]) is dict)
#         self.assertTrue(type(response_data["matches_offer"][0]["match_events"]) is list)
#         self.assertTrue(type(response_data["matches_offer"][0]["race_tickets"]) is list)
#         self.assertTrue(type(response_data["matches_offer"][0]["match_events"][0]["match"]) is dict)
#         self.assertTrue(type(response_data["matches_offer"][0]["match_events"][0]["event"]) is dict)
#
#         # deep analysis offer
#         self.assertTrue(type(response_data["deep_analysis_offer"]) is list)
#         self.assertEqual(len(response_data["deep_analysis_offer"]), 14)
#         self.assertTrue(type(response_data["deep_analysis_offer"][0]["race_tickets"]) is list)
#         self.assertTrue(type(response_data["deep_analysis_offer"][0]["match_events"]) is list)
#         self.assertTrue(type(response_data["deep_analysis_offer"][0]["collection"]) is dict)
#
#         # played race tickets
#         self.assertTrue(type(response_data["played_race_tickets"]) is list)
#         self.assertEqual(len(response_data["played_race_tickets"]), 0)

    # def test_user_request_a_not_existing_user_ticket(self):
    #     pass
    #
    # def test_user_fills_requested_user_ticket_just_created(self):
    #     pass
    #
    # def test_user_checks_offer_with_played_tickets(self):
    #     pass
    #
    # def test_user_request_an_existing_user_ticket(self):
    #     pass
    #
    # def test_user_modifies_requested_user_ticket(self):
    #     pass
