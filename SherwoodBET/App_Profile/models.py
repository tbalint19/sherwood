from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.db import models
from App_Account.models import Account

class ProfileManager(models.Manager):

    def create_profile(self, username, email, password, inviter):
        user = User.objects.create_user(username=username, email=email, password=password)
        Account(user_obj=user).save()
        profile = Profile(user_obj=user).set_confirmation_code()
        profile.save()
        Invitation.objects.create_if_possible(profile, inviter)
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

class InvitationManager(models.Manager):

    def create_if_possible(self, invited, inviter):
        try:
            profile = User.objects.get(username=inviter).profile
        except User.DoesNotExist:
            profile = None
        if profile is not None:
            Invitation(inviter=profile, invited=invited).save()
        return profile is not None


class Invitation(models.Model):

    inviter = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='inviter')
    invited = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='invited')

    objects = InvitationManager()

    def __str__(self):
        return str(self.inviter) + " - " + str(self.invited)
