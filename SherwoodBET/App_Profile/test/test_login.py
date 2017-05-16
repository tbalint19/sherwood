from django.contrib.auth.models import AnonymousUser, User
from django.test import TestCase, RequestFactory
from django.core.urlresolvers import reverse
from App_Profile.models import Profile, Account
from App_Profile import views
import json

class LoginDataFactory:

    def json(self, username="DefaultInDB", email="Default@indb.hu", password="12345Ab", missing=None, credential="username"):
        data = {'password': password}
        data[credential] = vars()[credential]
        if missing is not None:
            del data[missing]
        return json.dumps(data)

class LoginTestUser:

    def __init__(self, client):
        self.client = client

    def post(self, data):
        return self.client.post(reverse('login_user'), data, content_type='application/json')

class Login_test(TestCase):

    def setUp(self):
        self.user = LoginTestUser(self.client)
        self.factory = LoginDataFactory()
        self.user_in_db = User.objects.create_user(
            username='DefaultInDB', email='Default@indb.hu', password='12345Ab')

    def test_sunny_day_login(self):
        data = self.factory.json()
        response = self.user.post(data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content.decode('utf-8'))['content'], {'is_successful': True})

    def test_wrong_password(self):
        data = self.factory.json(password="54321Ab")
        response = self.user.post(data)
        self.assertEqual(json.loads(response.content.decode('utf-8'))['content'], {'is_successful': False})

    def test_sunny_day_login_email(self):
        data = self.factory.json(credential="email")
        response = self.user.post(data)
        self.assertEqual(json.loads(response.content.decode('utf-8'))['content'], {'is_successful': True})