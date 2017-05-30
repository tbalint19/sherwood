from django.test import TestCase, tag
from _Test.util.user import TestUser
from _Test.util.data import TestData
from _Test.util.test_data.first_offer import first_offer
from App_Profile.models import *
from App_Game.models import *
import json

@tag('story')
class TestStory(TestCase):

    @classmethod
    def setUpTestData(cls):
        data = TestData()
        data.create_teams();                    cls.set_up_1 = list(Team.objects.all())
        data.create_events();                   cls.set_up_2 = list(Event.objects.all())
        data.create_matches();                  cls.set_up_3 = list(Match.objects.all())
        data.create_final_result_events();      cls.set_up_4 = list(MatchEvent.objects.all())
        data.create_derby_events();             cls.set_up_5 = list(MatchEvent.objects.all())
        data.create_collections();              cls.set_up_6 = list(Collection.objects.all())
        data.add_matches_to_collection();       cls.set_up_7 = list(MatchEventOfCollection.objects.all())
        data.add_events_to_collection();       cls.set_up_8 = list(MatchEventOfCollection.objects.all())
        data.create_race_tickets();             cls.set_up_9 = list(RaceTicket.objects.all())

        player_1 = TestUser()
        login_data = player_1.create_login_data('Bela12', '123456Ab');
        cls.response_1 = player_1.request_login(login_data)

        login_data = player_1.create_login_data('bela@bela.hu', '123456Ab')
        cls.response_2 = player_1.request_login(login_data)

        signup_data = player_1.create_signup_data('Bela12', 'bela@bela.hu', '123456Ab', None)
        cls.response_3 = player_1.request_singnup(signup_data)

        cls.status_1 = {'users': len(Profile.objects.all()), 'invitations': len(Invitation.objects.all())}

        signup_data = player_1.create_signup_data('Bela12', 'bela@lajos.hu', '123456Ab', None)
        cls.response_4 = player_1.request_singnup(signup_data)

        signup_data = player_1.create_signup_data('Lajos12', 'bela@bela.hu', '123456Ab', None)
        cls.response_5 = player_1.request_singnup(signup_data)

        signup_data = player_1.create_signup_data('Bela12', 'bela@bela.hu', '123456Ab', None)
        cls.response_6 = player_1.request_singnup(signup_data)

        cls.status_2 = {'users': len(Profile.objects.all()), 'invitations': len(Invitation.objects.all())}

        signup_data = player_1.create_signup_data('Lajos12', 'lajos@lajos.hu', '123456Ab', 'Bela12')
        cls.response_7 = player_1.request_singnup(signup_data)

        cls.status_3 = {'users': len(Profile.objects.all()), 'invitations': len(Invitation.objects.all())}

        signup_data = player_1.create_signup_data('Kazmer12', 'kazmer@kazmer.hu', '123456Ab', 'Otto12')
        cls.response_8 = player_1.request_singnup(signup_data)

        cls.status_4 = {'users': len(Profile.objects.all()), 'invitations': len(Invitation.objects.all())}

        login_data = player_1.create_login_data('Bela12', '123456Ab')
        cls.response_9 = player_1.request_login(login_data)
        cls.response_10 = player_1.request_logout()

        login_data = player_1.create_login_data('Bela12', '123456ACDEFg')
        cls.response_11 = player_1.request_login(login_data)

        login_data = player_1.create_login_data('bela@bela.hu', '123456ACDEFg')
        cls.response_12 = player_1.request_login(login_data)

        login_data = player_1.create_login_data('bela@bela.hu', '123456Ab')
        cls.response_13 = player_1.request_login(login_data)

        profile = Profile.objects.get(user_obj__username='Bela12')
        cls.status_5 = profile.is_confirmed
        confirm_data = player_1.create_confirm_data('Bela12', profile.confirmation_code)
        cls.response_14 = player_1.request_email_confirm(confirm_data)
        profile = Profile.objects.get(user_obj__username='Bela12')
        cls.status_6 = profile.is_confirmed

        profile = Profile.objects.get(user_obj__username='Kazmer12')
        cls.status_7 = profile.is_confirmed
        confirm_data = player_1.create_confirm_data('Kazmer12', profile.confirmation_code + "somethingelse")
        cls.response_15 = player_1.request_email_confirm(confirm_data)
        profile = Profile.objects.get(user_obj__username='Kazmer12')
        cls.status_8 = profile.is_confirmed

        cls.response_16 = player_1.request_offer()

        cls.status_9 = UserTicket.objects.all().exists()

        offer = json.loads(cls.response_16.content.decode('utf-8'))
        race_ticket_id = player_1.choose_matches_ticket(offer, "matches_offer", False, 100)
        cls.response_17 = player_1.request_user_ticket(race_ticket_id)

        cls.status_10 = UserTicket.objects.all().exists()

        cls.response_18 = player_1.request_user_ticket(race_ticket_id)

        cls.status_11 = list(UserTicket.objects.all())

    def setUp(self):
        self.maxDiff = None

    def test_teams_created(self):
        set_up = self.__class__.set_up_1
        self.assertEqual(len(set_up), 20)

    def test_teams_are_unique(self):
        set_up = self.__class__.set_up_1
        teams = set([str(team) for team in set_up])
        self.assertEqual(len(set_up), len(teams))

    def test_events_created(self):
        set_up = self.__class__.set_up_2
        self.assertEqual(len(set_up), 7)

    def test_events_are_unique(self):
        set_up = self.__class__.set_up_2
        events = set([str(event) for event in set_up])
        self.assertEqual(len(set_up), len(events))

    def test_matches_created(self):
        set_up = self.__class__.set_up_3
        self.assertEqual(len(set_up), 7)

    def test_matches_are_unique(self):
        set_up = self.__class__.set_up_3
        matches = set([str(match) for match in set_up])
        self.assertEqual(len(set_up), len(matches))

    def test_match_events_created(self):
        set_up = self.__class__.set_up_4
        self.assertEqual(len(set_up), 7)

    def test_match_events_are_unique(self):
        set_up = self.__class__.set_up_4
        match_events = set([str(match_event) for match_event in set_up])
        self.assertEqual(len(set_up), len(match_events))

    def test_derby_events_created(self):
        set_up = self.__class__.set_up_5
        self.assertEqual(len(set_up), 13)

    def test_match_events_are_unique_after_update(self):
        set_up = self.__class__.set_up_5
        match_events = set([str(match_event) for match_event in set_up])
        self.assertEqual(len(set_up), len(match_events))

    def test_collections_created(self):
        set_up = self.__class__.set_up_6
        self.assertEqual(len(set_up), 2)

    def test_collections_are_unique(self):
        set_up = self.__class__.set_up_6
        collections = set([str(collection) for collection in set_up])
        self.assertEqual(len(set_up), len(collections))

    def test_matches_added_to_collection(self):
        set_up = self.__class__.set_up_7
        self.assertEqual(len(set_up), 7)

    def test_matches_of_collections_are_unique(self):
        set_up = self.__class__.set_up_7
        objs = set([str(obj) for obj in set_up])
        self.assertEqual(len(set_up), len(objs))

    def test_events_added_to_collection(self):
        set_up = self.__class__.set_up_8
        self.assertEqual(len(set_up), 14)

    def test_events_of_collections_are_unique(self):
        set_up = self.__class__.set_up_8
        objs = set([str(obj) for obj in set_up])
        self.assertEqual(len(set_up), len(objs))

    def test_race_tickets_created(self):
        set_up = self.__class__.set_up_9
        self.assertEqual(len(set_up), 12)

    def test_race_tickets_are_unique(self):
        set_up = self.__class__.set_up_9
        objs = set([str(obj) for obj in set_up])
        self.assertEqual(len(set_up), len(objs))

    def test_user_tries_login_with_username_without_profile(self):
        response = self.__class__.response_1
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content.decode('utf-8')), {'is_successful': False})

    def test_user_tries_login_with_email_without_profile(self):
        response = self.__class__.response_2
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content.decode('utf-8')), {'is_successful': False})

    def test_user_signup_with_unoccupied_data(self):
        response = self.__class__.response_3
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content.decode('utf-8')), {'errors': []})

    def test_one_user_no_invitation(self):
        status = self.__class__.status_1
        self.assertEqual(status['users'], 1)
        self.assertEqual(status['invitations'], 0)

    def test_user_signup_with_occupied_username(self):
        response = self.__class__.response_4
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content.decode('utf-8')), {'errors': ["username"]})

    def test_user_signup_with_occupied_email(self):
        response = self.__class__.response_5
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content.decode('utf-8')), {'errors': ["email"]})

    def test_user_signup_with_occupied_username_and_email(self):
        response = self.__class__.response_6
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content.decode('utf-8')), {'errors': ["username", "email"]})

    def test_one_user_no_invitation_after_unsuccesful_attempts(self):
        status = self.__class__.status_2
        self.assertEqual(status['users'], 1)
        self.assertEqual(status['invitations'], 0)

    def test_user_signup_with_valid_inviter(self):
        response = self.__class__.response_7
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content.decode('utf-8')), {'errors': []})

    def test_two_user_one_invitation(self):
        status = self.__class__.status_3
        self.assertEqual(status['users'], 2)
        self.assertEqual(status['invitations'], 1)

    def test_user_signup_with_invalid_inviter(self):
        response = self.__class__.response_8
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content.decode('utf-8')), {'errors': []})

    def test_three_user_one_invitation(self):
        status = self.__class__.status_4
        self.assertEqual(status['users'], 3)
        self.assertEqual(status['invitations'], 1)

    def test_user_tries_login_with_valid_credentials_username(self):
        response = self.__class__.response_9
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content.decode('utf-8')), {'is_successful': True})

    def test_user_logout(self):
        response = self.__class__.response_10
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content.decode('utf-8')), {'is_successful': True})

    def test_user_tries_login_with_username_and_wrong_password(self):
        response = self.__class__.response_11
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content.decode('utf-8')), {'is_successful': False})

    def test_user_tries_login_with_email_and_wrong_password(self):
        response = self.__class__.response_12
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content.decode('utf-8')), {'is_successful': False})

    def test_user_tries_login_with_valid_credentials_email(self):
        response = self.__class__.response_13
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content.decode('utf-8')), {'is_successful': True})

    def test_user_is_not_confirmed(self):
        status = self.__class__.status_5
        self.assertFalse(status)

    def test_user_confirms_email(self):
        response = self.__class__.response_14
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content.decode('utf-8')), {'is_successful': True})

    def test_user_is_confirmed(self):
        status = self.__class__.status_6
        self.assertTrue(status)

    def test_other_user_is_not_confirmed(self):
        status = self.__class__.status_7
        self.assertFalse(status)

    def test_user_confirms_email_wrong_code(self):
        response = self.__class__.response_15
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content.decode('utf-8')), {'is_successful': False})

    def test_user_still_not_confirmed(self):
        status = self.__class__.status_8
        self.assertFalse(status)

    def test_offer_recieved_without_played_race_tickets(self):
        response = self.__class__.response_16
        response_data = json.loads(response.content.decode('utf-8'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(
            "played_race_tickets" in response_data and
            "matches_offer" in response_data and
            "deep_analysis_offer" in response_data)

    def test_no_played_race_tickets_in_offer(self):
        response = self.__class__.response_16
        response_data = json.loads(response.content.decode('utf-8'))
        self.assertEqual(len(response_data["played_race_tickets"]), 0)

    def test_offer_has_1_matches_offer(self):
        response = self.__class__.response_16
        response_data = json.loads(response.content.decode('utf-8'))
        self.assertEqual(len(response_data["matches_offer"]), 1)

    def test_offer_has_1_deep_analysis_offer(self):
        response = self.__class__.response_16
        response_data = json.loads(response.content.decode('utf-8'))
        self.assertEqual(len(response_data["deep_analysis_offer"]), 1)

    def test_offer_has_collection_info(self):
        response = self.__class__.response_16
        response_data = json.loads(response.content.decode('utf-8'))
        self.assertTrue(
            "collection" in response_data["matches_offer"][0] and
            "collection" in response_data["deep_analysis_offer"][0])

    def test_offer_has_race_ticket_info(self):
        response = self.__class__.response_16
        response_data = json.loads(response.content.decode('utf-8'))
        self.assertTrue(
            "race_tickets" in response_data["matches_offer"][0] and
            "race_tickets" in response_data["deep_analysis_offer"][0])

    def test_offer_has_6_matches_race_ticket(self):
        response = self.__class__.response_16
        response_data = json.loads(response.content.decode('utf-8'))
        self.assertEqual(len(response_data["matches_offer"][0]["race_tickets"]), 6)

    def test_offer_has_6_deep_analysis_race_ticket(self):
        response = self.__class__.response_16
        response_data = json.loads(response.content.decode('utf-8'))
        self.assertEqual(len(response_data["deep_analysis_offer"][0]["race_tickets"]), 6)

    def test_offer_has_match_event_info(self):
        response = self.__class__.response_16
        response_data = json.loads(response.content.decode('utf-8'))
        self.assertTrue(
            "match_events" in response_data["matches_offer"][0] and
            "match_events" in response_data["deep_analysis_offer"][0])

    def test_offer_has_7_match_events(self):
        response = self.__class__.response_16
        response_data = json.loads(response.content.decode('utf-8'))
        self.assertEqual(len(response_data["matches_offer"][0]["match_events"]), 7)
        self.assertEqual(len(response_data["deep_analysis_offer"][0]["match_events"]), 7)

    def test_offer_has_match_info_in_match_event_info(self):
        response = self.__class__.response_16
        response_data = json.loads(response.content.decode('utf-8'))
        self.assertTrue(
            "match" in response_data["deep_analysis_offer"][0]["match_events"][0] and
            "match" in response_data["matches_offer"][0]["match_events"][0])

    def test_offer_has_event_info_in_match_event_info(self):
        response = self.__class__.response_16
        response_data = json.loads(response.content.decode('utf-8'))
        self.assertTrue(
            "event" in response_data["deep_analysis_offer"][0]["match_events"][0] and
            "event" in response_data["matches_offer"][0]["match_events"][0])

    def test_full_offer_first(self):
        response = self.__class__.response_16
        response_data = json.loads(response.content.decode('utf-8'))
        self.assertEqual(response_data, first_offer)

    def test_user_tickets_do_not_exist(self):
        status = self.__class__.status_9
        self.assertFalse(status)

    def test_choosing_first_not_existing_user_ticket_response_arrives(self):
        response = self.__class__.response_17
        self.assertEqual(response.status_code, 200)

    def test_user_ticket_to_fill_has_userticket_info(self):
        response = self.__class__.response_17
        self.assertTrue("user_ticket" in json.loads(response.content.decode('utf-8')))

    def test_user_ticket_to_fill_has_bet_info(self):
        response = self.__class__.response_17
        self.assertTrue("related_bets" in json.loads(response.content.decode('utf-8')))

    def test_7_bets(self):
        response = self.__class__.response_17
        response_data = json.loads(response.content.decode('utf-8'))
        bets = response_data["related_bets"]
        self.assertEqual(len(bets), 7)

    def test_bet_has_all_related_info(self):
        response = self.__class__.response_17
        response_data = json.loads(response.content.decode('utf-8'))
        bets = response_data["related_bets"]
        self.assertTrue("bet_data" in bets[0] and "match_data" in bets[0] and "event_data" in bets[0])

    def test_user_ticket_exists(self):
        status = self.__class__.status_10
        self.assertTrue(status)

    def test_choosing_first_existing_user_ticket_response_arrives(self):
        response = self.__class__.response_18
        self.assertEqual(response.status_code, 200)

    def test_user_ticket_not_recreated(self):
        status = self.__class__.status_11
        self.assertEqual(len(status), 1)
