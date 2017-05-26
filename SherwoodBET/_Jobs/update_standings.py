from App_Game.models import *

def update_standings():
    for collection in Collection.objects.filter(status=Collection.PLAYABLE):
        collection.set_live_if_needed()
    for collection in Collection.objects.filter(status=Collection.LIVE):
        collection.set_finished_if_needed()
        for race_ticket in RaceTicket.objects.get_for_collection(collection):
            for user_ticket in race_ticket.user_tickets.all():
                user_ticket.update_points()
            race_ticket.sort_related_user_tickets()
