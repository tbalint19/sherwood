from App_Game.requests import OfferRequest, TicketRequest, BetRequest
from App_Game.models import Collection, UserTicket
from _Middleware import API


@API.endpoint(OfferRequest)
def get_offer(request):
    return {
        "matches_offer": Collection.objects.get_offer(is_deep_analysis=False),
        "deep_analysis_offer": Collection.objects.get_offer(is_deep_analysis=True),
        "played_race_tickets": UserTicket.objects.get_played_race_tickets(request.user)}


@API.endpoint(TicketRequest)
def get_ticket(request):
    user_ticket = UserTicket.objects.get_or_create_user_ticket(request.user, request.race_ticket)
    if not user_ticket.paid and not request.user.account.has_sufficient_funds(race_ticket=request.race_ticket):
        return {"error": "Insufficient funds"}
    return {
        "user_ticket": user_ticket,
        "related_bets": user_ticket.get_or_create_related_bets()}


@API.endpoint(BetRequest)
def place_bet(request):
    request.user.account.pay_user_ticket_if_needed_and_possible(request.user_ticket)
    if not request.user_ticket.paid:
        return {"error": "Insufficient funds"}
    for bet in request.bets:
        bet_data = [data for data in request.bet_data if data["id"] == bet.id][0]
        bet.update(bet_data['home'], bet_data['draw'], bet_data['away'])
    return {"error": None}
