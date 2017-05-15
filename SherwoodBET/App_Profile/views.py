from django.contrib.auth.models import User
from App_Profile.models import Profile, Account
from _Middleware import API
import json

@API.public
def signup_user(request):
    user_data = json.loads(request.body.decode('utf-8'))
    if not "username" in user_data or not "email" in user_data or not "password" in user_data:
        return {'errors': []}
    if len(user_data["username"]) < 7 or len(user_data["email"]) < 7 or len(user_data["password"]) < 7:
        return {'errors': []}
    if len(user_data["username"]) > 50 or len(user_data["email"]) > 50 or len(user_data["password"]) > 50:
        return {'errors': []}
    number_of_ats = len(["@" for letter in user_data["email"] if letter == "@"])
    if number_of_ats != 1:
        return {'errors': []}
    email_name = user_data["email"].split("@")[0]
    email_domain = user_data["email"].split("@")[1]
    email = email_name + "@" + email_domain.lower()
    errors = list(filter(None, [
        "username" if User.objects.filter(username=user_data["username"]).exists() else None,
        "email" if User.objects.filter(email=email).exists() else None]))
    if not errors:
        user = User.objects.create_user(
            username=user_data['username'], password=user_data['password'], email=user_data['email'])
        Profile.objects.create_profile(user)
        Account(user_obj=user).save()
    return {'errors': errors}

@API.public
def login_user(request):
    pass

@API.user
def logout_user(request):
    pass
