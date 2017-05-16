import json
import string

class LoginRequest:

    def get_from_request(self, request):
        return json.loads(request.body.decode('utf-8'))
