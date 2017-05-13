from django.contrib.auth.models import AnonymousUser, User
from django.test import TestCase, RequestFactory
from django.core.urlresolvers import reverse
from . import views
import json

class User_test(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.user_in_db = User.objects.create_user(
            username='x', email='x@x.hu', password='123456Xy')

    def test_signup_sunnyday(self):
        request_data = json.dumps({'username': "bela", 'password': "123456Bela", 'email': "bela@x.hu"})
        response = self.client.post(reverse('signup_user'), data=request_data, content_type='application/json')
        user_exists = User.objects.filter(username="bela").exists()
        self.assertEqual(user_exists, True)
