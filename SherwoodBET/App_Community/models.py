from django.db import models
from django.contrib.auth.models import User, AnonymousUser
from App_Game.models import Collection

class Championship(models.Model):

    name = models.CharField(max_length=30)
    number_of_rounds = models.IntegerField()
    current_season = models.IntegerField(default=1)

    def get_current_round(self):
        season_obj = self.seasons.get(number=self.current_season)
        round_obj = season_obj.rounds.get(number=season_obj.current_round)
        collection_obj = round_obj.collection_obj
        race_ticket_obj = collection_obj.race_ticket_obj
        return {'collection': collection_obj, 'race_ticket': race_ticket_obj}


class Season(models.Model):

    chamionship_obj = models.ForeignKey(Championship, on_delete=models.CASCADE, related_name="seasons")
    champion_obj = models.ForeignKey(User, on_delete=models.CASCADE)
    number = models.IntegerField()
    current_round = models.IntegerField(default=1)

class Round(models.Model):

    season_obj = models.ForeignKey(Season, on_delete=models.CASCADE, related_name="rounds")
    collection_obj = models.ForeignKey(Collection, on_delete=models.CASCADE)
    number = models.IntegerField()

class Competitor(models.Model):

    chamionship_obj = models.ForeignKey(Championship, on_delete=models.CASCADE, related_name="competitors")
    user_obj = models.ForeignKey(User, on_delete=models.CASCADE)
    is_admin = models.BooleanField(default=False)
    is_confirmed = models.BooleanField(default=False)
    rank = models.IntegerField(null=True, default=None)

class FriendShipManager(models.Manager):

    def get_for_user(self, user):
        all_requested = self.filter(requester=user)
        all_received = self.filter(receiver=user)
        return [user for user in all_requested] + [user for user in all_received]

class FriendShip(models.Model):

    requester = models.ForeignKey(User, on_delete=models.CASCADE, related_name="requester")
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="receiver")
    is_confirmed = models.BooleanField(default=False)

    objects = FriendShipManager()
