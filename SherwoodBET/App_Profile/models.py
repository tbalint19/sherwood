from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):

    user_obj = models.OneToOneField(User, on_delete=models.CASCADE)
    rank = models.CharField(max_length=20, default="newbie")
    annual_points = models.IntegerField(default=0)
    monthly_points = models.IntegerField(default=0)

class Account(models.Model):

    user_obj = models.OneToOneField(User, on_delete=models.CASCADE)
    game_money = models.IntegerField(default=1000)
    real_money = models.IntegerField(default=0)
