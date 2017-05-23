class TestPlayer:

    def __init__(self, client, username, email, password):
        self.client = client
        self.client.login(username=username, password=password)

    def request_singnup(self):
        signup_data = {}
        return self.client.post(reverse('signup_user'), signup_data, content_type='application/json')

    def request_login(self):
        login_data = {}
        return self.client.post(reverse('login_user'), login_data, content_type='application/json')

    def request_logout(self):
        return self.client.get(reverse('logout_user'))

    def request_offer(self):
        return self.client.get(reverse('get_offer'))

    def request_ticket(self, race_ticket_id):
        return self.client.get('/game/api/get_ticket?race_ticket_id=' + race_ticket_id)

    def request_bet(self, data):
        bet = self.play(data)
        return self.client.post(reverse('place_bet'), bet, content_type='application/json')

    def play(self, game_data):
        for bet in game_data["related_bets"]:
            bet["bet_data"]["home"] = 70
            bet["bet_data"]["draw"] = 20
            bet["bet_data"]["away"] = 10
        return game_data
