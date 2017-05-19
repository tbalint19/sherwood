from django.shortcuts import render
from App_Game.requests import OfferRequest
from App_Game.models import Collection, UserTicket
from _Middleware import API

@API.endpoint(OfferRequest)
def get_offer(user):
    return {
        "matches_offer": Collection.objects.get_offer(is_deep_analysis=False),
        "deep_analysis_offer": Collection.objects.get_offer(is_deep_analysis=True),
        "played_race_tickets": UserTicket.objects.get_played_race_tickets(user)}
