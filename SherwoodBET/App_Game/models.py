from django.db import models
from django.contrib.auth.models import User, AnonymousUser

class Team(models.Model):

    name = models.CharField(max_length=50, unique=True)
    short_name = models.CharField(max_length=15, unique=True)
    stadium = models.CharField(max_length=50)

    def __str__(self):
        return self.short_name

class Match(models.Model):
    UPCOMING = "Upcoming"
    LIVE = "Live"
    OVER = "Over"
    status_choices = ((UPCOMING, "Upcoming"), (LIVE, "Live"), (OVER, "Over"))

    home_team_obj = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="home_team")
    away_team_obj = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="away_team")
    league = models.CharField(max_length=30, default="Friendly")
    round = models.CharField(max_length=10, default="", blank=True)
    link = models.CharField(max_length=100, default="", blank=True)
    deadline = models.DateTimeField()
    status = models.CharField(max_length=8, choices=status_choices, default=UPCOMING)

    def __str__(self):
        return str(self.home_team_obj) + " - " + str(self.away_team_obj)

class Event(models.Model):

    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class MatchEvent(models.Model):

    match_obj = models.ForeignKey(Match, on_delete=models.CASCADE, related_name="match_events")
    event_obj = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="match_events")
    result = models.CharField(max_length=5, blank=True, null=True)
    details = models.CharField(max_length=5, blank=True, null=True)

    def __str__(self):
        return str(self.match_obj) + " / " + str(self.event_obj)

class CollectionManager(models.Manager):

    def get_offer(self, is_deep_analysis):
        return [
            {"collection": collection, "match_events": [{
            "match":obj.match_event_obj.match_obj,
            "event": obj.match_event_obj.event_obj}
            for obj in collection.match_events.all()],
            "race_tickets": [race_ticket for race_ticket in collection.race_tickets.all()]}
            for collection in self.filter(status=Collection.PLAYABLE, is_deep_analysis=is_deep_analysis)]

class Collection(models.Model):
    HIDDEN = "Hidden"
    PLAYABLE = "Playable"
    LIVE = "Live"
    FINISHED = "Finished"
    status_choices = ((HIDDEN, "Hidden"), (PLAYABLE, "Playable"), (LIVE, "Live"), (FINISHED, "Finished"))

    number = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=30)
    intro = models.CharField(max_length= 300)
    status = models.CharField(max_length=8, choices=status_choices, default=HIDDEN)
    is_deep_analysis = models.BooleanField(default=False)

    objects = CollectionManager()

    def __str__(self):
        return "#" + str(self.number) + ": " + self.title

    def set_live_if_needed(self):
        if self.match_events.filter(match_event_obj__match_obj__status=Match.LIVE).exists():
            self.status = Collection.LIVE
            self.save()

    def set_finished_if_needed(self):
        if not self.match_events.filter(match_event_obj__match_obj__status=Match.OVER).exists():
            self.status = Collection.FINISHED
            self.save()

class MatchEventOfCollection(models.Model):

    collection_obj = models.ForeignKey(Collection, on_delete=models.CASCADE, related_name='match_events')
    match_event_obj = models.ForeignKey(MatchEvent, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.match_event_obj) + " of " + str(self.collection_obj)

class RaceTicketManager(models.Manager):

    def get_for_collection(self, collection):
        race_tickets = []
        for is_prof in [True, False]:
            for amount in [1, 10, 100]:
                try:
                    race_tickets.append(self.get(
                        collection_obj=collection, bet_amount=amount, is_professional=is_prof))
                except RaceTicket.DoesNotExist:
                    continue
        return race_tickets

class RaceTicket(models.Model):

    collection_obj = models.ForeignKey(Collection, on_delete=models.CASCADE, related_name='race_tickets')
    is_professional = models.BooleanField()
    bet_amount = models.IntegerField()
    number_of_competitors = models.IntegerField(default=0)

    objects = RaceTicketManager()

    def __str__(self):
        return str(self.collection_obj) + " / " + str(self.bet_amount)

class UserTicketManager(models.Manager):

    def get_played_race_tickets(self, user):
        return [
            user_ticket.race_ticket_obj
            for user_ticket in self.filter(
            user_obj=None if user == AnonymousUser() else user, paid=True,
            race_ticket_obj__collection_obj__status=Collection.PLAYABLE)]

    def get_or_create_user_ticket(self, user, race_ticket):
        user_ticket = self.get_or_create(user_obj=user, race_ticket_obj=race_ticket)[0]
        user_ticket.save()
        return user_ticket

    def get_results(self, user, params):
        user_tickets = self.filter(user_obj=user)
        if "status" in params:
            user_tickets = user_tickets.filter(race_ticket_obj__collection_obj__status=params['status'])
        if "is_professional" in status:
            user_tickets = user_tickets.filter(race_ticket_obj__is_professional=params['is_professional'])
        if "bet_amount" in params:
            user_tickets = user_tickets.filter(race_ticket_obj__bet_amount=params['bet_amount'])
        if "min_payoff" in params:
            user_tickets = user_tickets.filter(payoff__gte=params['min_payoff'])
        if "max_payoff" in params:
            user_tickets = user_tickets.filter(payoff__lte=params['max_payoff'])
        if len(user_tickets[params['present']:]) > 12:
            return user_tickets[params['present']:][:12]
        return [
            {"user_ticket": user_ticket, "related_race_ticket": user_ticket.race_ticket_obj}
            for user_ticket in user_tickets[params['present']:]]


class UserTicket(models.Model):

    race_ticket_obj = models.ForeignKey(RaceTicket, on_delete=models.CASCADE, related_name='user_tickets')
    user_obj = models.ForeignKey(User, on_delete=models.CASCADE)
    points = models.BigIntegerField(default=1)
    rank = models.IntegerField(null=True, blank=True, default=None)
    payoff = models.FloatField(null=True, blank=True, default=None)
    paid = models.BooleanField(default=False)

    objects = UserTicketManager()

    def __str__(self):
        return self.user_obj.username + "'s " + str(self.race_ticket_obj)

    def __lt__(self, other):
        if self.result == other.result:
            return self.id > other.id
        return self.result > other.result

    def get_or_create_related_bets(self):
        related_bets = []
        for obj in self.race_ticket_obj.collection_obj.match_events.all():
            bet = Bet.objects.get_or_create_bet(self, obj.match_event_obj)
            related_bets.append(
                {"bet_data": bet,
                "match_data": bet.match_event_obj.match_obj,
                "event_data": bet.match_event_obj.event_obj})
        return related_bets

    def get_bet_results(self):
        return [{
            "bet_data": bet,
            "match_data": bet.match_event_obj.match_obj,
            "event_data": bet.match_event_obj.event_obj} for bet in self.bets.all()]

class BetManager(models.Manager):

    def get_or_create_bet(self, user_ticket, match_event):
        bet = self.get_or_create(user_ticket_obj=user_ticket, match_event_obj=match_event)[0]
        bet.save()
        return bet

class Bet(models.Model):

    match_event_obj = models.ForeignKey(MatchEvent, on_delete=models.CASCADE)
    user_ticket_obj = models.ForeignKey(UserTicket, on_delete=models.CASCADE, related_name='bets')
    home = models.IntegerField(default=0)
    draw = models.IntegerField(default=0)
    away = models.IntegerField(default=0)
    result = models.IntegerField(default=1)

    objects = BetManager()

    def __str__(self):
        return str(self.user_ticket_obj) + " - " + str(self.match_event_obj)

    def update(self, home, draw, away):
        self.home = home
        self.draw = draw
        self.away = away
        self.save()
