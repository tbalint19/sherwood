from _Middleware import APP, API

@APP.entry
def get_home(request):
    return {'public': "login", 'protected': "wall"}
