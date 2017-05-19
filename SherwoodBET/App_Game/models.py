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

class Event(models.Model):

    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class MatchEvent(models.Model):

    match_obj = models.ForeignKey(Match, on_delete=models.CASCADE)
    event_obj = models.ForeignKey(Event, on_delete=models.CASCADE)
    result = models.CharField(max_length=5, blank=True, null=True)
    details = models.CharField(max_length=5, blank=True, null=True)

    def __str__(self):
        return str(self.match_obj) + " / " + str(self.event_obj)

class Collection(models.Model):

    number = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=30)
    intro = models.CharField(max_length= 300)
    hidden = models.BooleanField(default=True)
    playable = models.BooleanField(default=False)
    live = models.BooleanField(default=False)
    finished = models.BooleanField(default=False)
    deep_analysis = models.BooleanField(default=False)

    def __str__(self):
        return "#" + str(self.number) + ": " + self.title
