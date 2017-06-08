from django.conf.urls import url
from . import views


urlpatterns = [

     # tickets
    url(r'^api/get_offer', views.get_offer, name='get_public_offer'),
    url(r'^api/get_ticket', views.get_ticket, name='get_ticket'),

    # bet
    url(r'^api/place_bet', views.place_bet, name='place_bet'),

    # usertickets
    url(r'^api/get_user_ticket_results', views.get_user_ticket_results, name='get_user_ticket_results'),
    # url(r'^api/get_ticket', views.get_ticket, name='get_ticket'),

    # numbers for homepage
    url(r'^api/get_archive_numbers', views.get_archive_numbers, name='get_archive_numbers'),

]
