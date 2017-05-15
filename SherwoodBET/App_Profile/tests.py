from django.contrib.auth.models import AnonymousUser, User
from django.test import TestCase, RequestFactory
from django.core.urlresolvers import reverse
from App_Profile.models import Profile, Account
from . import views
import json

class SignupDataFactory:

    def create_json(self, username="NewUser1", email="new@user1.com", password="12345Ab", missing=None):
        data = {'username': username, 'email': email, 'password': password}
        if missing is not None:
            del data[missing]
        return json.dumps(data)


class User_test(TestCase):

    def setUp(self):
        self.factory = SignupDataFactory()
        self.user_in_db = User.objects.create_user(
            username='DefaultInDB', email='Default@indb.hu', password='123456Ab')
        Profile(user_obj=self.user_in_db).save()
        Account(user_obj=self.user_in_db).save()

    def test_signup_sunnyday(self):
        request_data = self.factory.create_json()
        response = self.client.post(reverse('signup_user'), data=request_data, content_type='application/json')
        user_exists = User.objects.filter(username="NewUser1").exists()
        self.assertTrue(user_exists)
        self.assertEqual(json.loads(response.content.decode('utf-8'))['content'], {'errors': []})

    def test_signup_same_username(self):
        request_data = self.factory.create_json(username="DefaultInDB")
        response = self.client.post(reverse('signup_user'), data=request_data, content_type='application/json')
        users = User.objects.filter(username="DefaultInDB")
        self.assertEqual(len(users), 1)
        self.assertEqual(json.loads(response.content.decode('utf-8'))['content'], {'errors': ["username"]})

    def test_signup_same_email(self):
        request_data = self.factory.create_json(email="Default@indb.hu")
        response = self.client.post(reverse('signup_user'), data=request_data, content_type='application/json')
        users = User.objects.filter(email="Default@indb.hu")
        self.assertEqual(len(users), 1)
        self.assertEqual(json.loads(response.content.decode('utf-8'))['content'], {'errors': ["email"]})

    def test_signup_same_credentials(self):
        request_data = self.factory.create_json(username="DefaultInDB", email="Default@indb.hu")
        response = self.client.post(reverse('signup_user'), data=request_data, content_type='application/json')
        errors = json.loads(response.content.decode('utf-8'))['content']['errors']
        self.assertTrue("username" in errors and "email" in errors)

    def test_user_extensions_created(self):
        request_data = self.factory.create_json()
        response = self.client.post(reverse('signup_user'), data=request_data, content_type='application/json')
        profile_exists = Profile.objects.filter(user_obj__username="NewUser1").exists()
        account_exists = Account.objects.filter(user_obj__username="NewUser1").exists()
        self.assertTrue(profile_exists)
        self.assertTrue(account_exists)

    def test_user_extension_with_proper_data(self):
        request_data = self.factory.create_json()
        response = self.client.post(reverse('signup_user'), data=request_data, content_type='application/json')
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
        request_data = self.factory.create_json(username="DefaultInDB")
        response = self.client.post(reverse('signup_user'), data=request_data, content_type='application/json')
        profiles = Profile.objects.filter(user_obj__username="DefaultInDB")
        accounts = Account.objects.filter(user_obj__username="DefaultInDB")
        self.assertEqual(len(profiles), 1)
        self.assertEqual(len(accounts), 1)

    def test_invalid_signup_data_username_missing(self):
        request_data = self.factory.create_json(missing='username')
        response = self.client.post(reverse('signup_user'), data=request_data, content_type='application/json')
        user_exists = User.objects.filter(email="new@user1.hu").exists()
        self.assertFalse(user_exists)
        self.assertEqual(json.loads(response.content.decode('utf-8'))['content'], {'errors': []})

    def test_invalid_signup_data_email_missing(self):
        request_data = self.factory.create_json(missing='email')
        response = self.client.post(reverse('signup_user'), data=request_data, content_type='application/json')
        user_exists = User.objects.filter(username="NewUser1").exists()
        self.assertFalse(user_exists)
        self.assertEqual(json.loads(response.content.decode('utf-8'))['content'], {'errors': []})

    def test_invalid_signup_data_password_missing(self):
        request_data = self.factory.create_json(missing='password')
        response = self.client.post(reverse('signup_user'), data=request_data, content_type='application/json')
        user_exists = User.objects.filter(email="NewUser1").exists()
        self.assertFalse(user_exists)
        self.assertEqual(json.loads(response.content.decode('utf-8'))['content'], {'errors': []})

    def test_signup_with_short_username(self):
        request_data = self.factory.create_json(username='only6c')
        response = self.client.post(reverse('signup_user'), data=request_data, content_type='application/json')
        user_exists = User.objects.filter(username="only6c").exists()
        self.assertFalse(user_exists)
        self.assertEqual(json.loads(response.content.decode('utf-8'))['content'], {'errors': []})

    def test_signup_with_short_email(self):
        request_data = self.factory.create_json(email='A1@2.3')
        response = self.client.post(reverse('signup_user'), data=request_data, content_type='application/json')
        user_exists = User.objects.filter(email="1@2.3").exists()
        self.assertFalse(user_exists)
        self.assertEqual(json.loads(response.content.decode('utf-8'))['content'], {'errors': []})

    def test_signup_with_short_password(self):
        request_data = self.factory.create_json(password='only6c')
        response = self.client.post(reverse('signup_user'), data=request_data, content_type='application/json')
        user_exists = User.objects.filter(username="KovacsBela").exists()
        self.assertFalse(user_exists)
        self.assertEqual(json.loads(response.content.decode('utf-8'))['content'], {'errors': []})

    def test_signup_with_long_username(self):
        request_data = self.factory.create_json(username=''.join(["B" for x in range(51)]))
        response = self.client.post(reverse('signup_user'), data=request_data, content_type='application/json')
        user_exists = User.objects.filter(email="new@user1.hu").exists()
        self.assertFalse(user_exists)
        self.assertEqual(json.loads(response.content.decode('utf-8'))['content'], {'errors': []})

    def test_signup_with_long_email(self):
        request_data = self.factory.create_json(username=''.join(["B" for x in range(46)]) + "@x.hu")
        response = self.client.post(reverse('signup_user'), data=request_data, content_type='application/json')
        user_exists = User.objects.filter(username="NewUser1").exists()
        self.assertFalse(user_exists)
        self.assertEqual(json.loads(response.content.decode('utf-8'))['content'], {'errors': []})

    def test_signup_with_long_password(self):
        request_data = self.factory.create_json(password=''.join(["B" for x in range(51)]))
        response = self.client.post(reverse('signup_user'), data=request_data, content_type='application/json')
        user_exists = User.objects.filter(username="KovacsBela").exists()
        self.assertFalse(user_exists)
        self.assertEqual(json.loads(response.content.decode('utf-8'))['content'], {'errors': []})

    def test_signup_with_invalid_email(self):
        request_data = self.factory.create_json(email="onlychar")
        response = self.client.post(reverse('signup_user'), data=request_data, content_type='application/json')
        user_exists = User.objects.filter(email="onlychar").exists()
        self.assertFalse(user_exists)

    def test_signup_with_upper_domain_email(self):
        request_data = self.factory.create_json(email="with@upper.com")
        self.client.post(reverse('signup_user'), data=request_data, content_type='application/json')
        request_data = self.factory.create_json(email="with@UPPER.com", username="NewUser2")
        response = self.client.post(reverse('signup_user'), data=request_data, content_type='application/json')
        errors = json.loads(response.content.decode('utf-8'))['content']['errors']
        user_exists_with_upper = User.objects.filter(email="with@UPPER.com").exists()
        user_exists_with_lower = User.objects.filter(email="with@upper.com").exists()
        self.assertFalse(user_exists_with_upper)
        self.assertTrue(user_exists_with_lower)
        self.assertEqual(len(User.objects.filter(username="NewUser1")), 1)
        self.assertEqual(len(User.objects.filter(username="NewUser2")), 0)
        self.assertEqual(len(User.objects.filter(email="with@upper.com")), 1)
