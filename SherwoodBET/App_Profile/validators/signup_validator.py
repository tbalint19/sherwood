import json
import string

class SignupRequestValidator:

    def __init__(self):
        self.user_data = None
        self.username_chars = string.ascii_letters + string.digits + "_"
        self.email_name_chars = string.ascii_letters + string.digits + "."
        self.email_domain_chars = string.ascii_lowercase + "."
        self.password_chars = string.ascii_letters + string.digits + "_" + "@" + "-" + "&" + "/" + "*"

    def validate(self, request):
        try:
            method_is_valid = self.check_method(request)
            self.parse(request)
            username_is_valid = self.check_username()
            email_is_valid = self.check_email()
            password_is_valid = self.check_password()
            if method_is_valid and username_is_valid and email_is_valid and password_is_valid:
                return self.user_data
            return None
        except:
            return None

    def check_method(self, request):
        return request.method == "POST"

    def parse(self, request):
        self.user_data = json.loads(request.body.decode('utf-8'))

    def check_username(self):
        if not "username" in self.user_data:
            return False
        if not isinstance(self.user_data["username"], str):
            return False
        if len(self.user_data['username']) < 7 or len(self.user_data['username']) > 20:
            return False
        for letter in self.user_data["username"]:
            if letter not in self.username_chars:
                return False
        return True

    def check_email(self):
        if not "email" in self.user_data:
            return False
        email = self.user_data["email"]
        if not isinstance(email, str):
            return False
        if len(email) < 7 or len(email) > 75:
            return False
        if len(["@" for letter in email if letter == "@"]) != 1:
            return False
        email_name = email.split("@")[0]
        email_domain = email.split("@")[1]
        for letter in email_name:
            if letter not in self.email_name_chars:
                return False
        for letter in email_domain:
            if letter not in self.email_domain_chars:
                return False
        return True

    def check_password(self):
        if not "password" in self.user_data:
            return False
        password = self.user_data["password"]
        if not isinstance(password, str):
            return False
        if len(password) < 7 or len(password) > 20:
            return False
        for letter in password:
            if letter not in self.password_chars:
                return False
        return True
