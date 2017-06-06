from django.test import Client
from django.urls import reverse
from App_Profile.models import Profile
from App_Profile.views import signup_user, login_user, logout_user, get_profile_data
import random
import json

class TestUser:

    def __init__(self):
        self.client = Client()

    def create_signup_data(self, username, email, password, inviter):
        return {'username': username, 'email': email, 'password': password, 'inviter': inviter}

    def request_singnup(self, signup_data):
        return self.client.post(reverse('signup_user'), json.dumps(signup_data), content_type='application/json')

    def create_login_data(self, credential, password):
        return {'identification': credential, 'password': password}

    def request_login(self, login_data):
        return self.client.post(reverse('login_user'), json.dumps(login_data), content_type='application/json')

    def create_confirm_data(self, username, confirmation_code):
        return {'username': username, 'confirmation_code': confirmation_code}

    def request_email_confirm(self, confirm_data):
        return self.client.post(reverse('confirm_user'), json.dumps(confirm_data), content_type='application/json')

    def request_logout(self):
        return self.client.get(reverse('logout_user'))

    def request_profile_data(self):
        return self.client.get(reverse('get_profile_data'))

    def request_account_data(self):
        return self.client.get(reverse('get_account_data'))

    def request_offer(self):
        return self.client.get(reverse('get_offer'))

    def choose_matches_ticket(self, offer, offer_type, is_professional, bet_amount):
        race_tickets = offer[offer_type][0]["race_tickets"]
        for race_ticket in race_tickets:
            if race_ticket["is_professional"] == is_professional and race_ticket["bet_amount"] == bet_amount:
                return race_ticket["id"]

    def request_user_ticket(self, race_ticket_id):
        return self.client.get('/game/api/get_ticket?race_ticket_id=' + str(race_ticket_id))

    def play(self, game_data):
        for bet in game_data["related_bets"]:
            avg_70 = random.randint(40, 100)
            avg_15_1 = random.randint(0, 100 - avg_70)
            avg_15_2 = 100 - avg_70 - avg_15_1
            bet["bet_data"]["home"] = avg_15_1
            bet["bet_data"]["draw"] = avg_15_2
            bet["bet_data"]["away"] = avg_70
        return game_data

    def request_bet(self, data):
        bet = self.play(data)
        return self.client.post(reverse('place_bet'), json.dumps(bet), content_type='application/json')

    def filter_own_user_tickets(self, status=None, is_prof=None, amount=None, min=None, max=None, present=0):
        params = "?present=" + str(present)
        return params

    def request_own_tickets(self, params):
        return self.client.get('/game/api/get_user_ticket_results' + params)

    def request_own_ticket(self):
        pass
