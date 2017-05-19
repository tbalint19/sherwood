from django.db import models
from django.contrib.auth.models import User

class Team(models.Model):

    name = models.CharField(max_length=50, unique=True)
    short_name = models.CharField(max_length=15, unique=True)
    stadium = models.CharField(max_length=50)

    def __str__(self):
        return self.short_name

class Match(models.Model):

    home_team_obj = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="home_team")
    away_team_obj = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="away_team")
    league = models.CharField(max_length=30, default="Friendly")
    round = models.CharField(max_length=10, default="", blank=True)
    link = models.CharField(max_length=100, default="", blank=True)
    deadline = models.DateTimeField()
    upcoming = models.BooleanField(default=True)
    live = models.BooleanField(default=False)
    over = models.BooleanField(default=False)

    def __str__(self):
        return str(self.home_team_obj) + " - " + str(self.away_team_obj)
