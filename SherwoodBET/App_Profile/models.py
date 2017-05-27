from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.db import models
import random
import string

class ProfileManager(models.Manager):

    def create_profile(self, username, email, password, inviter=None):
        user = User.objects.create_user(username=username, email=email, password=password)
        Account(user_obj=user).save()
        Profile(user_obj=user).set_confirmation_code().save()
        Invitation.objects.create_if_possible(user, inviter)
        return user

    def check_if_possible(self, username, email):
        return list(filter(None, [
            "username" if self.filter(user_obj__username=username).exists() else None,
            "email" if self.filter(user_obj__email=email).exists() else None]))

    def authenticate_user(self, request, credential, password):
        if "@" in credential:
            if self.filter(user_obj__email=credential).exists():
                username = self.get(user_obj__email=credential).user_obj.username
                return authenticate(request, username=username, password=password)
            return None
        return authenticate(request, username=credential, password=password)

    def confirm_user(self, confirmation_code, username):
        try:
            profile = self.get(confirmation_code=confirmation_code, user_obj__username=username)
        except Profile.DoesNotExist:
            profile = None
        if profile is not None:
            profile.is_confirmed = True
            profile.save()
        return profile is not None


class Profile(models.Model):

    user_obj = models.OneToOneField(User, on_delete=models.CASCADE)
    rank = models.CharField(max_length=20, default="newbie")
    annual_points = models.IntegerField(default=0)
    monthly_points = models.IntegerField(default=0)
    is_confirmed = models.BooleanField(default=False)
    confirmation_code = models.CharField(max_length=25, default=None, blank=True, null=True)
    email_sent = models.BooleanField(default=False)
    email_attempted = models.BooleanField(default=False)

    objects = ProfileManager()

    def __str__(self):
        return self.user_obj.username + "'s profile'"

    def set_confirmation_code(self):
        self.confirmation_code = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(25))
        return self

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
            is_possible = self.has_sufficient_funds(user_ticket.race_ticket)
            if is_possible:
                self.pay_user_ticket(user_ticket)

    def pay_user_ticket(self, user_ticket):
        if user_ticket.race_ticket.is_professional:
            self.real_money -= user_ticket.race_ticket.bet_amount
        else:
            self.game_money -= user_ticket.race_ticket.bet_amount
        user_ticket.paid = True
        self.save()
        user_ticket.save()

class InvitationManager(models.Manager):

    def create_if_possible(self, invited, inviter):
        try:
            user = User.objects.get(username=inviter)
        except User.DoesNotExist:
            user = None
        if user is not None:
            Invitation(inviter=user, invited=invited).save()
        return user is not None


class Invitation(models.Model):

    inviter = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='inviter')
    invited = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='invited')

    objects = InvitationManager()

    def __str__(self):
        return str(self.inviter) + " - " + str(self.invited)
