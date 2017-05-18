from django.http import JsonResponse
import json

class API:

    @classmethod
    def endpoint(cls, Expected):
        def validate(view):
            def create_response(request):
                arg = Expected().get_from_request(request)
                if not arg:
                    return JsonResponse({}, status=404)
                response = cls.create_template()
                response['is_authenticated'] = cls.authenticate(request, Expected.auth_status)
                if response['is_authenticated'] is not False:
                    response['content'] = view(arg)
                return JsonResponse(response)
            return create_response
        return validate

    @staticmethod
    def create_template():
        return {'content': None, 'is_authenticated': None}

    @staticmethod
    def authenticate(request, auth_status):
        if auth_status == "user":
            return request.user.is_authenticated
        if auth_status == "admin":
            return request.user.is_superuser
        return None
