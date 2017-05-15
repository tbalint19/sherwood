import json

class SignupRequestValidator:

    def validate(self, request):
        try:
            user_data = json.loads(request.body.decode('utf-8'))
        except:
            return None
        if not "username" in user_data or not "email" in user_data or not "password" in user_data:
            return None
        if len(user_data["username"]) < 7 or len(user_data["email"]) < 7 or len(user_data["password"]) < 7:
            return None
        if len(user_data["username"]) > 50 or len(user_data["email"]) > 50 or len(user_data["password"]) > 50:
            return None
        number_of_ats = len(["@" for letter in user_data["email"] if letter == "@"])
        if number_of_ats != 1:
            return None
        return user_data
