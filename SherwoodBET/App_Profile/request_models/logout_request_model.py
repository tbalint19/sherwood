import json
import string

class LogoutRequest:

    def get_from_request(self, request):
        return json.loads(request.body.decode('utf-8'))
