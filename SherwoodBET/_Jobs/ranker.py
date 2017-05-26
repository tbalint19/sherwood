class Ranker:
    def __init__(self, user_tickets):
        self.user_tickets = sorted(user_tickets)
        self.payoff_groups = self.create_payoff_groups()

    def rank(self, race_ticket):
        self.set_ranking()
        self.fill_payoff_groups_with_usertickets(payoff_groups, sorted_user_tickets)
        RaceTicket.set_payoff(payoff_groups)
        return self.user_ticket

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
        for payoff_group in payoff_groups:
            for spot_index in range(len(self.payoff_group)):
                payoff_group[spot_index] = self.user_tickets[ticket_index]
                ticket_index += 1

    def set_payoff(self):
        current_payoff = 20
        for payoff_group in self.payoff_groups:
            for user_ticket in payoff_group:
                user_ticket.payoff = current_payoff/10
                user_ticket.save()
            current_payoff -= 1
