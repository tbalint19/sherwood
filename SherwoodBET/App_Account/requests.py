import json
import string

class AccountRequest:

    auth_status = "user"
    request_method = "GET"

    def get_from_request(self, request):
        try:
            return request
        except:
            return None
