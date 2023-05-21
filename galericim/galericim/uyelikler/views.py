from django.shortcuts import render,redirect

def login_request(request):
    return render(request,"uyelikler/login.html")


def advert_request(request):
    return render(request,"uyelikler/advert.html")


def register_request(request):
    return render(request,"uyelikler/register.html")


def logout_request(request):
    return redirect("home")

def home_request(request):
    return render(request,"uyelikler/home.html")