from django.contrib.auth.models import AnonymousUser, User
from django.test import TestCase, RequestFactory
from django.core.urlresolvers import reverse
from App_Profile.models import Profile, Account
from App_Profile import views
import json

class SignupDataFactory:

    def json(self, username="NewUser1", email="new@user.com", password="12345Ab", missing=None):
        data = {'username': username, 'email': email, 'password': password}
        if missing is not None:
            del data[missing]
        return json.dumps(data)

class SignupTestUser:

    def __init__(self, client):
        self.client = client

    def post(self, data):
        return self.client.post(reverse('signup_user'), data, content_type='application/json')


class Signup_test(TestCase):

    def setUp(self):
        self.user_in_db = User.objects.create_user(
            username='DefaultInDB', email='Default@indb.hu', password='123456Ab')
        Profile(user_obj=self.user_in_db).save()
        Account(user_obj=self.user_in_db).save()
        self.user = SignupTestUser(self.client)
        self.factory = SignupDataFactory()

    def test_signup_sunnyday(self):
        response = self.user.post(self.factory.json())
        self.assertTrue(User.objects.filter(username="NewUser1").exists())
        self.assertEqual(json.loads(response.content.decode('utf-8'))['content'], {'errors': []})

    def test_signup_same_username(self):
        response = self.user.post(self.factory.json(username="DefaultInDB"))
        self.assertEqual(len(User.objects.filter(username="DefaultInDB")), 1)
        self.assertEqual(json.loads(response.content.decode('utf-8'))['content'], {'errors': ["username"]})

    def test_signup_same_email(self):
        response = self.user.post(self.factory.json(email="Default@indb.hu"))
        self.assertEqual(len(User.objects.filter(email="Default@indb.hu")), 1)
        self.assertEqual(json.loads(response.content.decode('utf-8'))['content'], {'errors': ["email"]})

    def test_signup_same_credentials(self):
        response = self.user.post(self.factory.json(username="DefaultInDB", email="Default@indb.hu"))
        errors = json.loads(response.content.decode('utf-8'))['content']['errors']
        self.assertTrue("username" in errors and "email" in errors)

    def test_user_extensions_created(self):
        response = self.user.post(self.factory.json())
        self.assertTrue(Profile.objects.filter(user_obj__username="NewUser1").exists())
        self.assertTrue(Account.objects.filter(user_obj__username="NewUser1").exists())

    def test_user_extension_with_proper_data(self):
        response = self.user.post(self.factory.json())
        profile = Profile.objects.get(user_obj__username="NewUser1")
        account = Account.objects.get(user_obj__username="NewUser1")
        self.assertEqual(profile.rank, "newbie")
        self.assertEqual(profile.monthly_points, 0)
        self.assertEqual(profile.annual_points, 0)
        self.assertFalse(profile.is_confirmed)
        self.assertEqual(len(profile.confirmation_code), 25)
        self.assertEqual(account.game_money, 1000)
        self.assertEqual(account.real_money, 0)

    def test_no_additional_extensions_created(self):
        response = self.client.post(self.factory.json(username="DefaultInDB"))
        self.assertEqual(len(Profile.objects.filter(user_obj__username="DefaultInDB")), 1)
        self.assertEqual(len(Account.objects.filter(user_obj__username="DefaultInDB")), 1)

    def test_invalid_signup_data_username_missing(self):
        response = self.user.post(self.factory.json(missing='username'))
        self.assertFalse(User.objects.filter(email="new@user1.hu").exists())
        self.assertEqual(json.loads(response.content.decode('utf-8')), {})

    def test_invalid_signup_data_email_missing(self):
        response = self.user.post(self.factory.json(missing='email'))
        self.assertFalse(User.objects.filter(username="NewUser1").exists())
        self.assertEqual(json.loads(response.content.decode('utf-8')), {})

    def test_invalid_signup_data_password_missing(self):
        response = self.user.post(self.factory.json(missing='password'))
        self.assertFalse(User.objects.filter(email="NewUser1").exists())
        self.assertEqual(json.loads(response.content.decode('utf-8')), {})

    def test_signup_with_short_username(self):
        response = self.user.post(self.factory.json(username='only6c'))
        self.assertFalse(User.objects.filter(username="only6c").exists())
        self.assertEqual(json.loads(response.content.decode('utf-8')), {})

    def test_signup_with_short_email(self):
        response = self.user.post(self.factory.json(email='A1@2.3'))
        self.assertFalse(User.objects.filter(email="1@2.3").exists())
        self.assertEqual(json.loads(response.content.decode('utf-8')), {})

    def test_signup_with_short_password(self):
        response = self.user.post(self.factory.json(password='only6c'))
        self.assertFalse(User.objects.filter(username="KovacsBela").exists())
        self.assertEqual(json.loads(response.content.decode('utf-8')), {})

    def test_signup_with_long_username(self):
        response = self.user.post(self.factory.json(username=''.join(["B" for x in range(51)])))
        self.assertFalse(User.objects.filter(email="new@user1.hu").exists())
        self.assertEqual(json.loads(response.content.decode('utf-8')), {})

    def test_signup_with_long_email(self):
        response = self.user.post(self.factory.json(username=''.join(["B" for x in range(46)]) + "@x.hu"))
        self.assertFalse(User.objects.filter(username="NewUser1").exists())
        self.assertEqual(json.loads(response.content.decode('utf-8')), {})

    def test_signup_with_long_password(self):
        response = self.user.post(self.factory.json(password=''.join(["B" for x in range(51)])))
        self.assertFalse(User.objects.filter(username="KovacsBela").exists())
        self.assertEqual(json.loads(response.content.decode('utf-8')), {})

    def test_signup_with_invalid_email(self):
        response = self.user.post(self.factory.json(email="onlychar"))
        self.assertFalse(User.objects.filter(email="onlychar").exists())
        self.assertEqual(json.loads(response.content.decode('utf-8')), {})

    def test_signup_with_upper_domain_email(self):
        self.user.post(self.factory.json(email="with@upper.com"))
        response = self.user.post(self.factory.json(email="with@UPPER.com", username="NewUser2"))
        self.assertFalse(User.objects.filter(email="with@UPPER.com").exists())
        self.assertTrue(User.objects.filter(email="with@upper.com").exists())
        self.assertEqual(len(User.objects.filter(username="NewUser1")), 1)
        self.assertEqual(len(User.objects.filter(username="NewUser2")), 0)
        self.assertEqual(len(User.objects.filter(email="with@upper.com")), 1)
