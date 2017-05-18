import json
import string

class LogoutRequest:

    auth_status = "user"
    request_method = "get"

    def get_from_request(self, request):
        return request
