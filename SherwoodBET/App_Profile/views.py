from App_Profile.requests import SignupRequest, LoginRequest, LogoutRequest
from App_Profile.models import Profile, Account
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from _Middleware import API
import json


@API.endpoint(SignupRequest)
def signup_user(user_data):
    errors = Profile.objects.check_if_possible(user_data['username'], user_data['email'])
    if not errors:
        Profile.objects.create_profile(user_data['username'], user_data['email'], user_data['password'])
    return {'errors': errors}


@API.endpoint(LoginRequest)
def login_user(request):
    user_data = json.loads(request.body.decode('utf-8'))
    user = Profile.objects.authenticate_user(request, user_data["identification"], user_data["password"])
    if user is not None:
        login(request, user)
    return {'is_successful': user is not None}


@API.endpoint(LogoutRequest)
def logout_user(request):
    logout(request)
    return {'is_successful': True}
