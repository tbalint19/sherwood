from App_Game.models import *

class Ranker:
    def __init__(self, user_tickets):
        self.user_tickets = sorted(user_tickets)
        self.payoff_groups = self.create_payoff_groups()

    def rank(self):
        self.set_ranking()
        self.fill_payoff_groups_with_usertickets()
        self.set_payoff()
        return self.user_tickets

    def set_ranking(self):
        for index, user_ticket in enumerate(self.user_tickets):
            user_ticket.rank = index + 1
            user_ticket.save()

    def create_payoff_groups(self):
        number_of_tickets = len(self.user_tickets)
        number_of_draws = int(number_of_tickets % 20)
        size_of_group = int((number_of_tickets - number_of_draws)/20)
        payoff_groups = [["empty_spot" for x in range(size_of_group)] for x in range(21)]
        payoff_groups[10] = ["empty_spot" for x in range(number_of_draws)]
        return payoff_groups

    def fill_payoff_groups_with_usertickets(self):
        ticket_index = 0
        for payoff_group in self.payoff_groups:
            for spot_index in range(len(payoff_group)):
                payoff_group[spot_index] = self.user_tickets[ticket_index]
                ticket_index += 1

    def set_payoff(self):
        current_payoff = 20
        for payoff_group in self.payoff_groups:
            for user_ticket in payoff_group:
                user_ticket.payoff = current_payoff/10
                user_ticket.save()
            current_payoff -= 1

def update_standings():
    for collection in Collection.objects.filter(status=Collection.PLAYABLE):
        collection.set_live_if_needed()
    for collection in Collection.objects.filter(status=Collection.LIVE):
        collection.set_finished_if_needed()
        for race_ticket in RaceTicket.objects.get_for_collection(collection):
            for user_ticket in race_ticket.user_tickets.all():
                user_ticket.update_points()
            race_ticket.sort_related_user_tickets()
