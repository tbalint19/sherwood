from django.conf.urls import url
from . import views


urlpatterns = [

     # tickets
    url(r'^api/get_offer', views.get_offer, name='get_private_offer'),

]
