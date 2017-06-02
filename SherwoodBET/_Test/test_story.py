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
        # initial offer created
        data = TestData()
        data.create_teams();                    cls.all_teams = list(Team.objects.all())
        data.create_events();                   cls.all_events = list(Event.objects.all())
        data.create_matches();                  cls.all_matches = list(Match.objects.all())
        data.create_final_result_events();      cls.all_final_result_events = list(MatchEvent.objects.all())
        data.create_derby_events();             cls.all_events_for_derby = list(MatchEvent.objects.all())
        data.create_collections();              cls.all_collections = list(Collection.objects.all())
        data.add_matches_to_collection();       cls.all_me_of_c_1 = list(MatchEventOfCollection.objects.all())
        data.add_events_to_collection();        cls.all_me_of_c_2 = list(MatchEventOfCollection.objects.all())
        data.create_race_tickets();             cls.all_race_tickets = list(RaceTicket.objects.all())

        # user attemps signup, login logout - with and without confirm, invitation
        player_1 = TestUser()
        login_data = player_1.create_login_data('Bela12', '123456Ab');
        cls.no_username_login_response = player_1.request_login(login_data)

        login_data = player_1.create_login_data('bela@bela.hu', '123456Ab')
        cls.no_email_login_response = player_1.request_login(login_data)

        signup_data = player_1.create_signup_data('Bela12', 'bela@bela.hu', '123456Ab', None)
        cls.correct_signup_response = player_1.request_singnup(signup_data)

        cls.all_profiles_1 = list(Profile.objects.all())
        cls.all_invitations_1 = list(Invitation.objects.all())

        signup_data = player_1.create_signup_data('Bela12', 'bela@lajos.hu', '123456Ab', None)
        cls.existing_username_signup_response = player_1.request_singnup(signup_data)

        signup_data = player_1.create_signup_data('Lajos12', 'bela@bela.hu', '123456Ab', None)
        cls.existing_email_signup_response = player_1.request_singnup(signup_data)

        signup_data = player_1.create_signup_data('Bela12', 'bela@bela.hu', '123456Ab', None)
        cls.existing_credentials_signup_response = player_1.request_singnup(signup_data)

        cls.all_profiles_2 = list(Profile.objects.all())
        cls.all_invitations_2 = list(Invitation.objects.all())

        signup_data = player_1.create_signup_data('Lajos12', 'lajos@lajos.hu', '123456Ab', 'Bela12')
        cls.existing_inviter_signup_response = player_1.request_singnup(signup_data)

        cls.all_profiles_3 = list(Profile.objects.all())
        cls.all_invitations_3 = list(Invitation.objects.all())

        signup_data = player_1.create_signup_data('Kazmer12', 'kazmer@kazmer.hu', '123456Ab', 'Otto12')
        cls.not_existing_inviter_signup_response = player_1.request_singnup(signup_data)

        cls.all_profiles_4 = list(Profile.objects.all())
        cls.all_invitations_4 = list(Invitation.objects.all())

        login_data = player_1.create_login_data('Bela12', '123456Ab')
        cls.correct_username_login_response = player_1.request_login(login_data)
        cls.correct_logout_response = player_1.request_logout()

        login_data = player_1.create_login_data('Bela12', '123456ACDEFg')
        cls.wrong_password_username_login_response = player_1.request_login(login_data)

        login_data = player_1.create_login_data('bela@bela.hu', '123456ACDEFg')
        cls.wrong_password_email_login_response = player_1.request_login(login_data)

        login_data = player_1.create_login_data('bela@bela.hu', '123456Ab')
        cls.correct_email_login_response = player_1.request_login(login_data)

        profile = Profile.objects.get(user_obj__username='Bela12')
        cls.user_is_confirmed_1 = profile.is_confirmed
        confirm_data = player_1.create_confirm_data('Bela12', profile.confirmation_code)
        cls.correct_confirm_response = player_1.request_email_confirm(confirm_data)
        profile = Profile.objects.get(user_obj__username='Bela12')
        cls.user_is_confirmed_2 = profile.is_confirmed

        profile = Profile.objects.get(user_obj__username='Kazmer12')
        cls.user_is_confirmed_3 = profile.is_confirmed
        confirm_data = player_1.create_confirm_data('Kazmer12', profile.confirmation_code + "somethingelse")
        cls.wrong_confirm_response = player_1.request_email_confirm(confirm_data)
        profile = Profile.objects.get(user_obj__username='Kazmer12')
        cls.user_is_confirmed_4 = profile.is_confirmed

        # the user plays
        cls.offer_response_without_played_tickets = player_1.request_offer()

        cls.all_user_tickets_1 = list(UserTicket.objects.all())
        offer = json.loads(cls.offer_response_without_played_tickets.content.decode('utf-8'))
        race_ticket_id = player_1.choose_matches_ticket(offer, "matches_offer", False, 100)
        cls.not_existing_userticket_response = player_1.request_user_ticket(race_ticket_id)
        cls.all_user_tickets_2 = list(UserTicket.objects.all())
        cls.existing_userticket_response = player_1.request_user_ticket(race_ticket_id)
        cls.all_user_tickets_3 = list(UserTicket.objects.all())

        cls.play_1 = player_1.play(json.loads(cls.existing_userticket_response.content.decode('utf-8')))
        cls.play_userticket_response = player_1.request_bet(cls.play_1)
        cls.all_bets_1 = list(Bet.objects.all())
        cls.all_game_money_user_tickets = list(UserTicket.objects.filter(race_ticket_obj__is_professional=False))

    def setUp(self):
        self.maxDiff = None

    def test_teams_created(self):
        all_teams = self.__class__.all_teams
        self.assertEqual(len(all_teams), 20)

    def test_teams_are_unique(self):
        all_teams = self.__class__.all_teams
        teams = set([str(team) for team in all_teams])
        self.assertEqual(len(all_teams), len(teams))

    def test_events_created(self):
        all_events = self.__class__.all_events
        self.assertEqual(len(all_events), 7)

    def test_events_are_unique(self):
        all_events = self.__class__.all_events
        events = set([str(event) for event in all_events])
        self.assertEqual(len(all_events), len(events))

    def test_matches_created(self):
        all_matches = self.__class__.all_matches
        self.assertEqual(len(all_matches), 7)

    def test_matches_are_unique(self):
        all_matches = self.__class__.all_matches
        matches = set([str(match) for match in all_matches])
        self.assertEqual(len(all_matches), len(matches))

    def test_match_events_created(self):
        all_final_result_events = self.__class__.all_final_result_events
        self.assertEqual(len(all_final_result_events), 7)

    def test_match_events_are_unique(self):
        all_final_result_events = self.__class__.all_final_result_events
        match_events = set([str(match_event) for match_event in all_final_result_events])
        self.assertEqual(len(all_final_result_events), len(match_events))

    def test_derby_events_created(self):
        all_events_for_derby = self.__class__.all_events_for_derby
        self.assertEqual(len(all_events_for_derby), 13)

    def test_match_events_are_unique_after_update(self):
        all_events_for_derby = self.__class__.all_events_for_derby
        match_events = set([str(match_event) for match_event in all_events_for_derby])
        self.assertEqual(len(all_events_for_derby), len(match_events))

    def test_collections_created(self):
        all_collections = self.__class__.all_collections
        self.assertEqual(len(all_collections), 2)

    def test_collections_are_unique(self):
        all_collections = self.__class__.all_collections
        collections = set([str(collection) for collection in all_collections])
        self.assertEqual(len(all_collections), len(collections))

    def test_matches_added_to_collection(self):
        all_me_of_c_1 = self.__class__.all_me_of_c_1
        self.assertEqual(len(all_me_of_c_1), 7)

    def test_matches_of_collections_are_unique(self):
        all_me_of_c_1 = self.__class__.all_me_of_c_1
        objs = set([str(obj) for obj in all_me_of_c_1])
        self.assertEqual(len(all_me_of_c_1), len(objs))

    def test_events_added_to_collection(self):
        all_me_of_c_2 = self.__class__.all_me_of_c_2
        self.assertEqual(len(all_me_of_c_2), 14)

    def test_events_of_collections_are_unique(self):
        all_me_of_c_2 = self.__class__.all_me_of_c_2
        objs = set([str(obj) for obj in all_me_of_c_2])
        self.assertEqual(len(all_me_of_c_2), len(objs))

    def test_race_tickets_created(self):
        all_race_tickets = self.__class__.all_race_tickets
        self.assertEqual(len(all_race_tickets), 12)

    def test_race_tickets_are_unique(self):
        all_race_tickets = self.__class__.all_race_tickets
        objs = set([str(obj) for obj in all_race_tickets])
        self.assertEqual(len(all_race_tickets), len(objs))

    def test_user_tries_login_with_username_without_profile(self):
        response = self.__class__.no_username_login_response
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content.decode('utf-8')), {'is_successful': False})

    def test_user_tries_login_with_email_without_profile(self):
        response = self.__class__.no_email_login_response
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content.decode('utf-8')), {'is_successful': False})

    def test_user_signup_with_unoccupied_data(self):
        response = self.__class__.correct_signup_response
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content.decode('utf-8')), {'errors': []})

    def test_one_user_no_invitation(self):
        profiles = self.__class__.all_profiles_1
        invitations = self.__class__.all_invitations_1
        self.assertEqual(len(profiles), 1)
        self.assertEqual(len(invitations), 0)

    def test_user_signup_with_occupied_username(self):
        response = self.__class__.existing_username_signup_response
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content.decode('utf-8')), {'errors': ["username"]})

    def test_user_signup_with_occupied_email(self):
        response = self.__class__.existing_email_signup_response
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content.decode('utf-8')), {'errors': ["email"]})

    def test_user_signup_with_occupied_username_and_email(self):
        response = self.__class__.existing_credentials_signup_response
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content.decode('utf-8')), {'errors': ["username", "email"]})

    def test_one_user_no_invitation_after_unsuccesful_attempts(self):
        profiles = self.__class__.all_profiles_2
        invitations = self.__class__.all_invitations_2
        self.assertEqual(len(profiles), 1)
        self.assertEqual(len(invitations), 0)

    def test_user_signup_with_valid_inviter(self):
        response = self.__class__.existing_inviter_signup_response
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content.decode('utf-8')), {'errors': []})

    def test_two_user_one_invitation(self):
        profiles = self.__class__.all_profiles_3
        invitations = self.__class__.all_invitations_3
        self.assertEqual(len(profiles), 2)
        self.assertEqual(len(invitations), 1)

    def test_user_signup_with_invalid_inviter(self):
        response = self.__class__.not_existing_inviter_signup_response
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content.decode('utf-8')), {'errors': []})

    def test_three_user_one_invitation(self):
        profiles = self.__class__.all_profiles_4
        invitations = self.__class__.all_invitations_4
        self.assertEqual(len(profiles), 3)
        self.assertEqual(len(invitations), 1)

    def test_user_tries_login_with_valid_credentials_username(self):
        response = self.__class__.correct_username_login_response
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content.decode('utf-8')), {'is_successful': True})

    def test_user_logout(self):
        response = self.__class__.correct_logout_response
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content.decode('utf-8')), {'is_successful': True})

    def test_user_tries_login_with_username_and_wrong_password(self):
        response = self.__class__.wrong_password_username_login_response
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content.decode('utf-8')), {'is_successful': False})

    def test_user_tries_login_with_email_and_wrong_password(self):
        response = self.__class__.wrong_password_email_login_response
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content.decode('utf-8')), {'is_successful': False})

    def test_user_tries_login_with_valid_credentials_email(self):
        response = self.__class__.correct_email_login_response
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content.decode('utf-8')), {'is_successful': True})

    def test_user_is_not_confirmed(self):
        user_is_confirmed = self.__class__.user_is_confirmed_1
        self.assertFalse(user_is_confirmed)

    def test_user_confirms_email(self):
        response = self.__class__.correct_confirm_response
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content.decode('utf-8')), {'is_successful': True})

    def test_user_is_confirmed(self):
        user_is_confirmed = self.__class__.user_is_confirmed_2
        self.assertTrue(user_is_confirmed)

    def test_other_user_is_not_confirmed(self):
        user_is_confirmed = self.__class__.user_is_confirmed_3
        self.assertFalse(user_is_confirmed)

    def test_user_confirms_email_wrong_code(self):
        response = self.__class__.wrong_confirm_response
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content.decode('utf-8')), {'is_successful': False})

    def test_user_still_not_confirmed(self):
        user_is_confirmed = self.__class__.user_is_confirmed_4
        self.assertFalse(user_is_confirmed)

    def test_offer_recieved_without_played_race_tickets(self):
        response = self.__class__.offer_response_without_played_tickets
        response_data = json.loads(response.content.decode('utf-8'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(
            "played_race_tickets" in response_data and
            "matches_offer" in response_data and
            "deep_analysis_offer" in response_data)

    def test_no_played_race_tickets_in_offer(self):
        response = self.__class__.offer_response_without_played_tickets
        response_data = json.loads(response.content.decode('utf-8'))
        self.assertEqual(len(response_data["played_race_tickets"]), 0)

    def test_offer_has_1_matches_offer(self):
        response = self.__class__.offer_response_without_played_tickets
        response_data = json.loads(response.content.decode('utf-8'))
        self.assertEqual(len(response_data["matches_offer"]), 1)

    def test_offer_has_1_deep_analysis_offer(self):
        response = self.__class__.offer_response_without_played_tickets
        response_data = json.loads(response.content.decode('utf-8'))
        self.assertEqual(len(response_data["deep_analysis_offer"]), 1)

    def test_offer_has_collection_info(self):
        response = self.__class__.offer_response_without_played_tickets
        response_data = json.loads(response.content.decode('utf-8'))
        self.assertTrue(
            "collection" in response_data["matches_offer"][0] and
            "collection" in response_data["deep_analysis_offer"][0])

    def test_offer_has_race_ticket_info(self):
        response = self.__class__.offer_response_without_played_tickets
        response_data = json.loads(response.content.decode('utf-8'))
        self.assertTrue(
            "race_tickets" in response_data["matches_offer"][0] and
            "race_tickets" in response_data["deep_analysis_offer"][0])

    def test_offer_has_6_matches_race_ticket(self):
        response = self.__class__.offer_response_without_played_tickets
        response_data = json.loads(response.content.decode('utf-8'))
        self.assertEqual(len(response_data["matches_offer"][0]["race_tickets"]), 6)

    def test_offer_has_6_deep_analysis_race_ticket(self):
        response = self.__class__.offer_response_without_played_tickets
        response_data = json.loads(response.content.decode('utf-8'))
        self.assertEqual(len(response_data["deep_analysis_offer"][0]["race_tickets"]), 6)

    def test_offer_has_match_event_info(self):
        response = self.__class__.offer_response_without_played_tickets
        response_data = json.loads(response.content.decode('utf-8'))
        self.assertTrue(
            "match_events" in response_data["matches_offer"][0] and
            "match_events" in response_data["deep_analysis_offer"][0])

    def test_offer_has_7_match_events(self):
        response = self.__class__.offer_response_without_played_tickets
        response_data = json.loads(response.content.decode('utf-8'))
        self.assertEqual(len(response_data["matches_offer"][0]["match_events"]), 7)
        self.assertEqual(len(response_data["deep_analysis_offer"][0]["match_events"]), 7)

    def test_offer_has_match_info_in_match_event_info(self):
        response = self.__class__.offer_response_without_played_tickets
        response_data = json.loads(response.content.decode('utf-8'))
        self.assertTrue(
            "match" in response_data["deep_analysis_offer"][0]["match_events"][0] and
            "match" in response_data["matches_offer"][0]["match_events"][0])

    def test_offer_has_event_info_in_match_event_info(self):
        response = self.__class__.offer_response_without_played_tickets
        response_data = json.loads(response.content.decode('utf-8'))
        self.assertTrue(
            "event" in response_data["deep_analysis_offer"][0]["match_events"][0] and
            "event" in response_data["matches_offer"][0]["match_events"][0])

    def test_full_offer_first(self):
        response = self.__class__.offer_response_without_played_tickets
        response_data = json.loads(response.content.decode('utf-8'))
        self.assertEqual(response_data, first_offer)

    def test_user_tickets_do_not_exist(self):
        all_user_tickets = self.__class__.all_user_tickets_1
        self.assertEqual(len(all_user_tickets), 0)

    def test_choosing_first_not_existing_user_ticket_response_arrives(self):
        response = self.__class__.not_existing_userticket_response
        self.assertEqual(response.status_code, 200)

    def test_user_ticket_to_fill_has_userticket_info(self):
        response = self.__class__.not_existing_userticket_response
        self.assertTrue("user_ticket" in json.loads(response.content.decode('utf-8')))

    def test_user_ticket_to_fill_has_bet_info(self):
        response = self.__class__.not_existing_userticket_response
        self.assertTrue("related_bets" in json.loads(response.content.decode('utf-8')))

    def test_7_bets(self):
        response = self.__class__.not_existing_userticket_response
        response_data = json.loads(response.content.decode('utf-8'))
        bets = response_data["related_bets"]
        self.assertEqual(len(bets), 7)

    def test_bet_has_all_related_info(self):
        response = self.__class__.not_existing_userticket_response
        response_data = json.loads(response.content.decode('utf-8'))
        bets = response_data["related_bets"]
        self.assertTrue("bet_data" in bets[0] and "match_data" in bets[0] and "event_data" in bets[0])

    def test_user_ticket_exists(self):
        all_user_tickets = self.__class__.all_user_tickets_2
        self.assertEqual(len(all_user_tickets), 1)

    def test_choosing_first_existing_user_ticket_response_arrives(self):
        response = self.__class__.existing_userticket_response
        self.assertEqual(response.status_code, 200)

    def test_user_ticket_not_recreated(self):
        all_user_tickets = self.__class__.all_user_tickets_3
        user_ticket = all_user_tickets[0]
        self.assertEqual(len(all_user_tickets), 1)
        self.assertFalse(user_ticket.paid)

    def test_user_played_bets(self):
        action = self.__class__.play_1
        bet = action["related_bets"][0]["bet_data"]
        self.assertEqual(bet["home"] + bet["draw"] + bet["away"], 100)

    def test_bet_response_arrives(self):
        response = self.__class__.play_userticket_response
        self.assertEqual(response.status_code, 200)

    def test_7_bets_after_fill(self):
        all_bets = self.__class__.all_bets_1
        self.assertEqual(len(all_bets), 7)

    def test_7_bets_filled_after_fill(self):
        all_bets = self.__class__.all_bets_1
        bets = [bet.home + bet.draw + bet.away for bet in all_bets]
        self.assertEqual(bets, [100, 100, 100, 100, 100, 100, 100])

    def test_user_ticket_paid_after_placed_bets(self):
        all_game_money_user_tickets = self.__class__.all_game_money_user_tickets
        user_ticket = all_game_money_user_tickets[0]
        self.assertEqual(len(all_game_money_user_tickets), 1)
        self.assertTrue(user_ticket.paid)
