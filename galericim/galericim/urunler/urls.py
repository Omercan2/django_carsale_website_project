from django.urls import path
from . import views

# http://127.0.0.1:8000/
# http://127.0.0.1:8000/home
# http://127.0.0.1:8000/advert
# http://127.0.0.1:8000/login
# http://127.0.0.1:8000/register



urlpatterns = [
    path("",views.home, name = "home"),
   # path("home",views.home),
    #path("advert",views.advert),
    #path("login",views.login),
    #path("register",views.register),
]