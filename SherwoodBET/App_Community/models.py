# from django.db import models
# from django.contrib.auth.models import User, AnonymousUser
#
# class PrivateRace(models.Model):
#
#     name = models.CharField(max_length=30)
#
# class MemberShip(models.Model):
#
#     group_obj = models.ForeignKey(PrivateRace, on_delete=models.CASCADE)
#     user_obj = models.ForeignKey(User, on_delete=models.CASCADE)
#     is_admin = models.BooleanField(default=False)
#     is_confirmed = models.BooleanField(default=False)
#     rank = models.IntegerField(null=True, default=None)
#
# class FriendShipManager(models.Manager):
#
#     def get_for_user(self, user):
#         all_requested = self.filter(requester=user)
#         all_received = self.filter(receiver=user)
#         return [user for user in all_requested] + [user for user in all_received]
#
# class FriendShip(models.Model):
#
#     requester = models.ForeignKey(User, on_delete=models.CASCADE, related_name="requester")
#     receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="receiver")
#     is_confirmed = models.BooleanField(default=False)
#
#     objects = FriendShipManager()
#
# class Donation(models.Model):
#
#     user_obj = models.ForeignKey(User, on_delete=models.CASCADE)
#
# class Preference(model.Model):
#
#     user_obj = models.ForeignKey(User, on_delete=models.CASCADE)
