from django.db import models
from django.contrib.auth.models import User
import random
import string

class ProfileManager(models.Manager):

    def create_profile(self, user):
        profile = Profile(user_obj=user)
        profile.set_confirmation_code()
        profile.save()
        return profile

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

class Account(models.Model):

    user_obj = models.OneToOneField(User, on_delete=models.CASCADE)
    game_money = models.IntegerField(default=1000)
    real_money = models.IntegerField(default=0)
