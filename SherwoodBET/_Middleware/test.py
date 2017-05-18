from django.contrib.auth.models import AnonymousUser, User
from django.test import TestCase, RequestFactory
from _Middleware import API, APP
import json

class ModelMock:

    def get_from_request(self, request):
        return True

class API_Test(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='x', email='x@x.hu', password='123456Xy')
        self.admin = User.objects.create_user(
            username='y', email='y@y.hu', password='123456xY', is_superuser=True)
        self.view = lambda request: "content"
        self.request_model = ModelMock

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
