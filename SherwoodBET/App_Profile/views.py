from App_Profile.requests import SignupRequest, LoginRequest, LogoutRequest
from App_Profile.models import Profile, Account
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from _Middleware import API
import json


@API.endpoint(SignupRequest)
def signup_user(request):
    errors = Profile.objects.check_if_possible(request.username, request.email)
    if not errors:
        Profile.objects.create_profile(request.username, request.email, request.password)
    return {'errors': errors}


@API.endpoint(LoginRequest)
def login_user(request):
    user = Profile.objects.authenticate_user(request, request.identification, request.password)
    if user is not None:
        login(request, user)
    return {"is_successful": user is not None}


@API.endpoint(LogoutRequest)
def logout_user(request):
    logout(request)
    return {'is_successful': True}
