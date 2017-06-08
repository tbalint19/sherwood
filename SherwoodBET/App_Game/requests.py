from App_Game.models import RaceTicket, UserTicket, Bet
import json

class OfferRequest:

    auth_status = "public"
    request_method = "GET"

    def get_from_request(self, request):
        try:
            return request
        except:
            return None

class RaceTicketRequest:

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
            game_data = json.loads(request.body.decode('utf-8'))
            request.user_ticket = UserTicket.objects.get(id=game_data["user_ticket"]["id"])
            request.bets = [Bet.objects.get(id=bet["bet_data"]["id"]) for bet in game_data["related_bets"]]
            request.bet_data = [bet["bet_data"] for bet in game_data["related_bets"]]
            return request
        except:
            return None        

class UserTicketsRequest:

    auth_status = "user"
    request_method = "GET"

    def get_from_request(self, request):
        try:
            request.params = {}
            request.params["present"] = int(request.GET.get("present"))
            return request
        except:
            return None

class UserTicketRequest:

    auth_status = "user"
    request_method = "GET"

    def get_from_request(self, request):
        try:
            return request
        except:
            return None

class ArchiveNumbersRequest:

    auth_status = "user"
    request_method = "GET"

    def get_from_request(self, request):
        try:
            return request
        except:
            return None
