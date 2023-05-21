from django.urls import path
from . import views

# http://127.0.0.1:8000/




urlpatterns = [
    path("",views.home, name = "home"),
   # path("home",views.home),
    #path("advert",views.advert),
    #path("login",views.login),
    #path("register",views.register),
]