from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from App_Profile.models import Profile, Account
from App_Profile.request_models import SignupRequest, LoginRequest
from _Middleware import API
import json

@API.public(expected=SignupRequest)
def signup_user(request):
    user_data = json.loads(request.body.decode('utf-8'))
    errors = Profile.objects.check_if_possible(user_data['username'], user_data['email'])
    if not errors:
        Profile.objects.create_profile(user_data['username'], user_data['email'], user_data['password'])
    return {'errors': errors}

@API.public(expected=LoginRequest)
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
