from django.conf.urls import url
from . import views


urlpatterns = [

    url(r'^api/get_account_data$', views.get_account_data, name='get_account_data'),

]
