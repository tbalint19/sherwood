from App_Game.requests import *
from App_Game.models import *
from _Middleware import API


@API.endpoint(OfferRequest)
def get_offer(request):
    return {
        "matches_offer": Collection.objects.get_offer(is_deep_analysis=False),
        "deep_analysis_offer": Collection.objects.get_offer(is_deep_analysis=True),
        "played_race_tickets": UserTicket.objects.get_played_race_tickets(request.user)}


@API.endpoint(RaceTicketRequest)
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


@API.endpoint(UserTicketsRequest)
def get_user_ticket_results(request):
    return {
        "user_tickets": UserTicket.objects.get_results(request.user, request.params)}


@API.endpoint(UserTicketRequest)
def get_user_ticket_result(request):
    return {
        "user_ticket": request.user_ticket,
        "related_race_ticket": request.user_ticket.race_ticket,
        "related_bets": request.user_ticket.get_bet_results()}


@API.endpoint(ArchiveNumbersRequest)
def get_archive_numbers(request):
    return {
        'archive_numbers': UserTicket.objects.get_numbers_for_user(request.user)}
