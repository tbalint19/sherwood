from django.db import models
from django.contrib.auth.models import User

class Account(models.Model):

    user_obj = models.OneToOneField(User, on_delete=models.CASCADE)
    game_money = models.IntegerField(default=1000)
    real_money = models.IntegerField(default=0)

    def __str__(self):
        return self.user_obj.username + "'s account'"

    def has_sufficient_funds(self, race_ticket):
        if race_ticket.is_professional:
            return race_ticket.bet_amount <= self.real_money
        return race_ticket.bet_amount <= self.game_money

    def pay_user_ticket_if_needed_and_possible(self, user_ticket):
        if not user_ticket.paid:
            is_possible = self.has_sufficient_funds(user_ticket.race_ticket_obj)
            if is_possible:
                self.pay_user_ticket(user_ticket)

    def pay_user_ticket(self, user_ticket):
        if user_ticket.race_ticket_obj.is_professional:
            self.real_money -= user_ticket.race_ticket_obj.bet_amount
        else:
            self.game_money -= user_ticket.race_ticket_obj.bet_amount
        user_ticket.paid = True
        self.save()
        user_ticket.save()

class Recipe(models.Model):

    user_obj = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.IntegerField()
    is_real_money = models.BooleanField()


class Donation(models.Model):

    user_obj = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.IntegerField()
