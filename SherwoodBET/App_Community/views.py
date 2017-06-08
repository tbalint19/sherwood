from App_Community.requests import *
from App_Community.models import *
from _Middleware import API


@API.endpoint(OfferRequest)
def get_offer(request):
    return {
        'championship_rounds': [competitor.championship.get_current_round() for
            competitor in Competitor.objects.filter(user_obj=request.user)]}
