from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from App_Profile.models import Profile, Account
from App_Profile.validators import SignupRequestValidator
from _Middleware import API
import json

@API.public
def signup_user(request):
    user_data = SignupRequestValidator().validate(request)
    if not user_data:
        return {'errors': []}
    username, email, password = user_data['username'], Profile.cleanse_email(user_data['email']), user_data['password']
    errors = Profile.objects.check_if_possible(username, email)
    if not errors:
        Profile.objects.create_profile(username, email, password)
    return {'errors': errors}

@API.public
def login_user(request):
    user_data = json.loads(request.body.decode('utf-8'))
    password = user_data["password"]
    if "username" in user_data:
        user = authenticate(request, username=user_data["username"], password=password)
    if "email" in user_data:
        user = authenticate(request, username=User.objects.get(email=user_data["email"]).username, password=password)
    is_authenticated = user is not None
    if is_authenticated:
        login(request, user)
    return {'is_successful': is_authenticated}

@API.user
def logout_user(request):
    pass
