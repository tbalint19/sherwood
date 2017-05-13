from django.contrib.auth.models import AnonymousUser, User
from django.test import TestCase, RequestFactory
from _Middleware import API, APP
import json

class API_Test(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='x', email='x@x.hu', password='123456Xy')
        self.admin = User.objects.create_user(
            username='y', email='y@y.hu', password='123456xY', is_superuser=True)
        self.view = lambda request: "content"

    def test_public_api_with_user(self):
        request = self.factory.get('/testroute')
        request.user = self.user
        response = API.public(self.view)(request)
        json_response = json.loads(response.content.decode('utf-8'))
        self.assertEqual(json_response['content'], "content")
        self.assertEqual(json_response['is_authenticated'], None)

    def test_public_api_without_user(self):
        request = self.factory.get('/testroute')
        request.user = AnonymousUser()
        response = API.public(self.view)(request)
        json_response = json.loads(response.content.decode('utf-8'))
        self.assertEqual(json_response['content'], "content")
        self.assertEqual(json_response['is_authenticated'], None)

    def test_user_api_without_user(self):
        request = self.factory.get('/testroute')
        request.user = AnonymousUser()
        response = API.user(self.view)(request)
        json_response = json.loads(response.content.decode('utf-8'))
        self.assertEqual(json_response['content'], None)
        self.assertEqual(json_response['is_authenticated'], False)

    def test_user_api_with_user(self):
        request = self.factory.get('/testroute')
        request.user = self.user
        response = API.user(self.view)(request)
        json_response = json.loads(response.content.decode('utf-8'))
        self.assertEqual(json_response['content'], 'content')
        self.assertEqual(json_response['is_authenticated'], True)

    def test_admin_api_without_user(self):
        request = self.factory.get('/testroute')
        request.user = AnonymousUser()
        response = API.admin(self.view)(request)
        json_response = json.loads(response.content.decode('utf-8'))
        self.assertEqual(json_response['content'], None)
        self.assertEqual(json_response['is_authenticated'], False)

    def test_admin_api_with_user(self):
        request = self.factory.get('/testroute')
        request.user = self.user
        response = API.admin(self.view)(request)
        json_response = json.loads(response.content.decode('utf-8'))
        self.assertEqual(json_response['content'], None)
        self.assertEqual(json_response['is_authenticated'], False)

    def test_admin_api_with_admin(self):
        request = self.factory.get('/testroute')
        request.user = self.admin
        response = API.admin(self.view)(request)
        json_response = json.loads(response.content.decode('utf-8'))
        self.assertEqual(json_response['content'], 'content')
        self.assertEqual(json_response['is_authenticated'], True)

class APP_Test(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='x', email='x@x.hu', password='123456Xy')
        self.admin = User.objects.create_user(
            username='y', email='y@y.hu', password='123456xY', is_superuser=True)

    def test_entry_app_without_user(self):
        request = self.factory.get('/testroute')
        request.user = AnonymousUser()
        response = APP.entry(lambda request: {'public': "login", 'protected': "wall"})(request)
        self.assertEqual(response.status_code, 200)

    def test_entry_app_with_user(self):
        request = self.factory.get('/testroute')
        request.user = self.user
        response = APP.entry(lambda request: {'public': "login", 'protected': "wall"})(request)
        self.assertEqual(response.status_code, 200)
