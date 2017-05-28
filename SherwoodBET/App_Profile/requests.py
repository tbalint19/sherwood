import json
import string

class SignupRequest:

    auth_status = "public"
    request_method = "POST"

    def __init__(self):
        self.user_data = None
        self.username_chars = string.ascii_letters + string.digits + "_"
        self.email_name_chars = string.ascii_letters + string.digits + "."
        self.email_domain_chars = string.ascii_lowercase + "."
        self.password_chars = string.ascii_letters + string.digits + "_" + "@" + "-" + "&" + "/" + "*"

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
        request.identification = json.loads(request.body.decode('utf-8'))["identification"]
        request.password = json.loads(request.body.decode('utf-8'))["password"]
        return request

class LogoutRequest:

    auth_status = "user"
    request_method = "GET"

    def get_from_request(self, request):
        return request

class EmailAuthRequest:

    auth_status = "public"
    request_method = "GET"

    def get_from_request(self, request):
        request.confirmation_code = request.GET.get("confirmation_code")
        request.username = request.GET.get("username")
        return request
