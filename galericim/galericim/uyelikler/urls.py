from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path("login",views.login_request,name="login"),
    path("home",views.home_request,name="user_home"),
    path("register",views.register_request,name="register"),
    path("logout",views.logout_request,name="logout"),
    path("advert",views.advert_request,name="advert"),
    path("info",views.info_request,name="info"),
]