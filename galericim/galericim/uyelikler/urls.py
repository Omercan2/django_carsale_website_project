from django.urls import path
from . import views

urlpatterns = [
    path("login",views.login_request,name="login"),
    path("home",views.home_request,name="user_home"),
    path("register",views.register_request,name="register"),
    path("logout",views.logout_request,name="logout"),
    path("advert",views.advert_request,name="advert"),

]