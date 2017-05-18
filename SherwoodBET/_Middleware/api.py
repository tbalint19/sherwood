from django.http import JsonResponse
import json

class API:

    @classmethod
    def endpoint(cls, Expected):
        def validate(view):
            def create_response(request):
                arg = Expected().get_from_request(request)
                if not arg:
                    return JsonResponse({}, status=403)
                if cls.is_authenticated(request, Expected.auth_status):
                    return JsonResponse(view(arg))
                return JsonResponse({}, status=401)
            return create_response
        return validate

    @staticmethod
    def is_authenticated(request, auth_status):
        if auth_status == "user":
            return request.user.is_authenticated
        if auth_status == "admin":
            return request.user.is_superuser
        return True
