from django.shortcuts import render
from App_Game.requests import OfferRequest, TicketRequest
from App_Game.models import Collection, UserTicket
from _Middleware import API

@API.endpoint(OfferRequest)
def get_offer(request):
    return {
        "matches_offer": Collection.objects.get_offer(is_deep_analysis=False),
        "deep_analysis_offer": Collection.objects.get_offer(is_deep_analysis=True),
        "played_race_tickets": UserTicket.objects.get_played_race_tickets(request.user)}

# @API.endpoint(TicketRequest)
# def get_ticket(request):
#     race_ticket = RaceTicket.objects.get(id=request.GET.get("race_ticket_id"))
#     user_ticket = UserTicket.objects.get_or_create_user_ticket(request.user, race_ticket)
#     if not user_ticket.paid and not request.user.account.has_sufficient_funds(race_ticket=race_ticket):
#         return {"error": "Insufficient funds"}
#     return {"user_ticket": dict(user_ticket), "related_bets": user_ticket.get_or_create_related_bets()}
