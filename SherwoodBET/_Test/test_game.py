from django.test import TestCase, Client
from _Test.player import TestPlayer
from App_Game.views import get_offer, get_ticket, place_bet

class TestProfile(TestCase):

    @classmethod
    def setUpTestData(cls):
        pass

    def setUp(self):
        pass

    def test_user_checks_offer_with_login_but_without_played_tickets(self):
        pass

    def test_user_request_a_not_existing_user_ticket(self):
        pass

    def test_user_fills_requested_user_ticket_just_created(self):
        pass

    def test_user_checks_offer_with_login_and_with_played_tickets(self):
        pass

    def test_user_request_an_existing_user_ticket(self):
        pass

    def test_user_modifies_requested_user_ticket(self):
        pass
