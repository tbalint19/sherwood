from django.test import Client
from django.urls import reverse
from App_Profile.models import Profile
from App_Profile.views import signup_user, login_user, logout_user
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

    def request_offer(self):
        return self.client.get(reverse('get_offer'))

    def request_user_ticket(self, race_ticket_id):
        return self.client.get('/game/api/get_ticket?race_ticket_id=' + race_ticket_id)

    def play(self, game_data):
        choices = [
            [80, 10, 10], [70, 20, 10], [40, 30, 30]
            [60, 30, 10], [50, 30, 20], [90, 10, 0]]
        for bet in game_data["related_bets"]:
            c = random.choice(choices)
            bet["bet_data"]["home"] = c[0]
            bet["bet_data"]["draw"] = c[1]
            bet["bet_data"]["away"] = c[2]
        return game_data

    def request_bet(self, data):
        bet = self.play(data)
        return self.client.post(reverse('place_bet'), bet, content_type='application/json')

    def request_own_tickets(self):
        pass

    def request_own_ticket(self):
        pass
