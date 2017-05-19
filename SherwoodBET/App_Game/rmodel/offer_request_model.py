class OfferRequest:

    auth_status = 'public'


    def get_from_request(self, request):
        return request.user
