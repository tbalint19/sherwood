from App_Account.requests import AccountRequest
from App_Account.models import Account
from _Middleware import API

@API.endpoint(AccountRequest)
def get_account_data(request):
    return {'account': request.user.account}
