from django.conf.urls import url
from . import views


urlpatterns = [

     # tickets
    url(r'^api/get_offer', views.get_offer, name='get_offer'),
    url(r'^api/get_ticket', views.get_ticket, name='get_ticket'),

    # bet
    url(r'^api/place_bet', views.place_bet, name='place_bet'),

    # usertickets
    # url(r'^api/get_tickets', views.get_tickets, name='get_tickets'),
    # url(r'^api/get_ticket', views.get_ticket, name='get_ticket'),

]
