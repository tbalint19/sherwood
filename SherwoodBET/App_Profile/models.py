from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.db import models
import random
import string

class ProfileManager(models.Manager):

    def create_profile(self, username, email, password):
        user = User.objects.create_user(
            username=username, email=email, password=password)
        Account(user_obj=user).save()
        Profile(user_obj=user).set_confirmation_code().save()
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

class Profile(models.Model):

    user_obj = models.OneToOneField(User, on_delete=models.CASCADE)
    rank = models.CharField(max_length=20, default="newbie")
    annual_points = models.IntegerField(default=0)
    monthly_points = models.IntegerField(default=0)
    is_confirmed = models.BooleanField(default=False)
    confirmation_code = models.CharField(max_length=25, default=None, blank=True, null=True)

    objects = ProfileManager()

    def set_confirmation_code(self):
        self.confirmation_code = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(25))
        return self

class Account(models.Model):

    user_obj = models.OneToOneField(User, on_delete=models.CASCADE)
    game_money = models.IntegerField(default=1000)
    real_money = models.IntegerField(default=0)
