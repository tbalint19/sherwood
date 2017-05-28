import json
import string

class SignupRequest:

    auth_status = "public"
    request_method = "POST"

    def get_from_request(self, request):
        try:
            request.username = json.loads(request.body.decode('utf-8'))['username']
            request.email = json.loads(request.body.decode('utf-8'))['email']
            request.password = json.loads(request.body.decode('utf-8'))['password']
            request.inviter = json.loads(request.body.decode('utf-8'))['inviter']
            return request
        except:
            return None

class LoginRequest:

    auth_status = "public"
    request_method = "POST"

    def get_from_request(self, request):
        try:
            request.identification = json.loads(request.body.decode('utf-8'))["identification"]
            request.password = json.loads(request.body.decode('utf-8'))["password"]
            return request
        except:
            return None

class LogoutRequest:

    auth_status = "user"
    request_method = "GET"

    def get_from_request(self, request):
        try:
            return request
        except:
            return None

class EmailAuthRequest:

    auth_status = "public"
    request_method = "POST"

    def get_from_request(self, request):
        try:
            request.confirmation_code = json.loads(request.body.decode('utf-8'))["confirmation_code"]
            request.username = json.loads(request.body.decode('utf-8'))["username"]
            return request
        except:
            return None
