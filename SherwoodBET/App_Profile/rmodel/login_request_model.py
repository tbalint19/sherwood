import json
import string

class LoginRequest:

    auth_status = "public"
    request_method = "post"

    def get_from_request(self, request):
        return request
