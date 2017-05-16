from django.http import JsonResponse
from django.http import Http404

class API:

    @staticmethod
    def create_template():
        return {'content': None, 'is_authenticated': None}

    @classmethod
    def public(cls, expected):
        def validate(view):
            def create_response(request):
                response = cls.create_template()
                valid_data = expected().get_from_request(request)
                if not valid_data:
                    return JsonResponse(response, status=404)
                else:
                    response['content'] = view(request)
                    return JsonResponse(response)
            return create_response
        return validate

    @classmethod
    def user(cls, expected):
        def validate(view):
            def create_response(request):
                response = cls.create_template()
                valid_data = expected().get_from_request(request)
                if not valid_data:
                    return JsonResponse(response, status=404)
                if request.user.is_authenticated:
                    response['content'] = view(request)
                    response['is_authenticated'] = True
                else:
                    response['is_authenticated'] = False
                return JsonResponse(response)
            return create_response
        return validate

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
