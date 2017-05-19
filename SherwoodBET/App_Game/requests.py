class OfferRequest:

    auth_status = "public"
    request_method = "get"

    def get_from_request(self, request):
        return request.user
