from django.http import JsonResponse
from _Serializer.serializer import Serializer as S
import json

class API:

    @classmethod
    def endpoint(cls, Expected):
        def validate(view):
            def create_response(request):
                if request.method != Expected.request_method:
                    return JsonResponse({}, status=404)
                request = Expected().get_from_request(request)
                if not request:
                    return JsonResponse({}, status=403)
                if not cls.is_authenticated(request, Expected.auth_status):
                    return JsonResponse({}, status=401)
                return JsonResponse(S.serialize(view(request)))
            return create_response
        return validate

    @staticmethod
    def is_authenticated(request, auth_status):
        if auth_status == "user":
            return request.user.is_authenticated
        if auth_status == "admin":
            return request.user.is_superuser
        return True
