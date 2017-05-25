from App_Game.models import RaceTicket

class OfferRequest:

    auth_status = "public"
    request_method = "GET"

    def get_from_request(self, request):
        try:
            return request
        except:
            return None

class TicketRequest:

    auth_status = "user"
    request_method = "GET"

    def get_from_request(self, request):
        try:
            request.race_ticket = RaceTicket.objects.get(id=int(request.GET.get("race_ticket_id")))
            return request
        except:
            return None

class BetRequest:

    auth_status = "user"
    request_method = "POST"

    def get_from_request(self, request):
        try:
            game_data = json.loads(request.body.decode("utf-8"))
            request.user_ticket = UserTicket.objects.get(id=game_data["user_ticket"]["id"])
            request.bets = []
            for bet in game_data["related_bets"]:
                request.bets.append(Bet.objects.get(id=bet["bet_data"]["id"]))
            request.bet_data = game_data["related_bets"]["bet_data"]
            return request
        except:
            return None
