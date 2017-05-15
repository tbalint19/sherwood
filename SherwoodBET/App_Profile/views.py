from django.contrib.auth.models import User
from App_Profile.models import Profile, Account
from App_Profile.validators import SignupRequestValidator
from _Middleware import API

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
    pass

@API.user
def logout_user(request):
    pass
