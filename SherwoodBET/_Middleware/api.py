from django.http import JsonResponse

class API:

    @staticmethod
    def create_template():
        return {'content': None, 'is_authenticated': None}

    @classmethod
    def public(cls, view):
        def create_response(request):
            response = cls.create_template()
            response['content'] = view(request)
            return JsonResponse(response)
        return create_response

    @classmethod
    def user(cls, view):
        def create_response(request):
            response = cls.create_template()
            if request.user.is_authenticated():
                response['content'] = view(request)
                response['is_authenticated'] = True
            else:
                response['is_authenticated'] = False
            return JsonResponse(response)
        return create_response

    @classmethod
    def admin(cls, view):
        def create_response(request):
            response = cls.create_template()
            if request.user.is_superuser:
                response['content'] = view(request)
                response['is_authenticated'] = True
            else:
                response['is_authenticated'] = False
            return JsonResponse(response)
        return create_response
