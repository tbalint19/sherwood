from django.conf.urls import url
from . import views


urlpatterns = [

    url(r'^api/signup$', views.signup_user, name='signup_user'),
    url(r'^api/login$', views.login_user, name='login_user'),
    url(r'^api/logout$', views.logout_user, name='logout_user'),
    url(r'^api/confirm$', views.confirm_user, name='confirm_user'),

]
