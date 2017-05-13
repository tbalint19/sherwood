from django.contrib.auth.models import User
from _Middleware import API
import json

@API.public
def signup_user(request):
    user_data = json.loads(request.body.decode('utf-8'))
    User(username=user_data['username'], password=user_data['password'], email=user_data['email']).save()

@API.public
def login_user(request):
    pass

@API.user
def logout_user(request):
    pass
