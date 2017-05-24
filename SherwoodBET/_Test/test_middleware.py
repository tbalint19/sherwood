from django.contrib.auth.models import AnonymousUser, User
from django.test import TestCase, RequestFactory
from _Middleware import API
import json

class ModelMock:

    auth_status = None
    request_method = None

    def get_from_request(self, request):
        if request.is_valid:
            return request
        return None

class TestAPI(TestCase):

    def setUp(self):
        self.maxDiff = None
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='x', email='x@x.hu', password='123456Xy')
        self.admin = User.objects.create_user(
            username='y', email='y@y.hu', password='123456xY', is_superuser=True)
        self.view = lambda request: {'content': "content"}

    def test_request_returns_json_with_http_404_if_method_is_wrong(self):
        request = self.factory.get('/testroute')
        ModelMock.request_method = "POST"
        response = API.endpoint(ModelMock)(self.view)(request)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(json.loads(response.content.decode('utf-8')), {})

    def test_invalid_request_returns_json_with_http_403(self):
        request = self.factory.get('/testroute')
        request.is_valid = False
        ModelMock.request_method = "GET"
        response = API.endpoint(ModelMock)(self.view)(request)
        self.assertEqual(response.status_code, 403)
        self.assertEqual(json.loads(response.content.decode('utf-8')), {})

    def test_valid_request_returns_json_with_http_200_on_public_for_anonymus(self):
        request = self.factory.get('/testroute')
        request.is_valid = True
        ModelMock.request_method = "GET"
        ModelMock.auth_status = "public"
        request.user = AnonymousUser()
        response = API.endpoint(ModelMock)(self.view)(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content.decode('utf-8')), {'content': "content"})

    def test_valid_request_returns_json_with_http_200_on_public_for_user(self):
        request = self.factory.get('/testroute')
        request.is_valid = True
        ModelMock.request_method = "GET"
        ModelMock.auth_status = "public"
        request.user = self.user
        response = API.endpoint(ModelMock)(self.view)(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content.decode('utf-8  ')), {'content': "content"})

    def test_valid_request_returns_json_with_http_200_on_public_for_admin(self):
        request = self.factory.get('/testroute')
        request.is_valid = True
        ModelMock.request_method = "GET"
        ModelMock.auth_status = "public"
        request.user = self.admin
        response = API.endpoint(ModelMock)(self.view)(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content.decode('utf-8')), {'content': "content"})

    def test_valid_request_returns_json_with_http_401_on_user_for_anonymus(self):
        request = self.factory.get('/testroute')
        request.is_valid = True
        ModelMock.request_method = "GET"
        ModelMock.auth_status = "user"
        request.user = AnonymousUser()
        response = API.endpoint(ModelMock)(self.view)(request)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(json.loads(response.content.decode('utf-8')), {})

    def test_valid_request_returns_json_with_http_200_on_user_for_user(self):
        request = self.factory.get('/testroute')
        request.is_valid = True
        ModelMock.request_method = "GET"
        ModelMock.auth_status = "user"
        request.user = self.user
        response = API.endpoint(ModelMock)(self.view)(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content.decode('utf-8')), {'content': "content"})

    def test_valid_request_returns_json_with_http_200_on_user_for_admin(self):
        request = self.factory.get('/testroute')
        request.is_valid = True
        ModelMock.request_method = "GET"
        ModelMock.auth_status = "user"
        request.user = self.admin
        response = API.endpoint(ModelMock)(self.view)(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content.decode('utf-8')), {'content': "content"})

    def test_valid_request_returns_json_with_http_401_on_admin_for_anonymus(self):
        request = self.factory.get('/testroute')
        request.is_valid = True
        ModelMock.request_method = "GET"
        ModelMock.auth_status = "admin"
        request.user = AnonymousUser()
        response = API.endpoint(ModelMock)(self.view)(request)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(json.loads(response.content.decode('utf-8')), {})

    def test_valid_request_returns_json_with_http_401_on_admin_for_user(self):
        request = self.factory.get('/testroute')
        request.is_valid = True
        ModelMock.request_method = "GET"
        ModelMock.auth_status = "admin"
        request.user = self.user
        response = API.endpoint(ModelMock)(self.view)(request)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(json.loads(response.content.decode('utf-8')), {})

    def test_valid_request_returns_json_with_http_200_on_admin_for_admin(self):
        request = self.factory.get('/testroute')
        request.is_valid = True
        ModelMock.request_method = "GET"
        ModelMock.auth_status = "admin"
        request.user = self.admin
        response = API.endpoint(ModelMock)(self.view)(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content.decode('utf-8')), {'content': "content"})
