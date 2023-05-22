from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from .forms import ArabaForm
from .models import Araba

def login_request(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username = username, password= password)
        if user is not None:
            login(request, user)
            return redirect("user_home")
        else:
            return render(request, "uyelikler/login.html",{
                "error": "Kullanıcı adı ya da Şifre hatalı"
            })
    return render(request,"uyelikler/login.html")


def advert_request(request):
    if request.method == 'POST':
        form = ArabaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_home')  # İlanların listelendiği bir sayfaya yönlendirme yapabilirsiniz
    else:
        form = ArabaForm()
    return render(request,"uyelikler/advert.html")


def register_request(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        password = request.POST["password"]
        repassword = request.POST["repassword"]

        if password == repassword:
            if User.objects.filter(username = username).exists():
                return render(request,"register", {"error":"Bu Kullanıcı Adı Kullanılıyor."})
            else:
                if User.objects.filter(email = email).exists():
                    return render(request,"register", {"error":"Bu E-Mail Kullanılıyor."})
                else:
                    user = User.objects.create_user(username=username,email=email,first_name=firstname,last_name=lastname,password=password)
                    user.save()
                    return redirect("login")
        else:
            return render(request,"register", {"error":"Parola eşleşmiyor."})
    return render(request,"uyelikler/register.html")


def logout_request(request):
    logout(request)
    return redirect("home")

def home_request(request):
    ilanlar = Araba.objects.all()
    context = {'ilanlar': ilanlar}
    return render(request, 'uyelikler/home.html', context)


def info_request(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        password = request.POST["password"]
        repassword = request.POST["repassword"]

        if password == repassword:
            user = get_object_or_404(User, username=username)
            user.email = email
            user.first_name = firstname
            user.last_name = lastname
            user.set_password(password)
            user.save()
            return redirect("user_home")
        else:
            return render(request, "uyelikler/info.html", {"error": "Parola eşleşmiyor."})
    return render(request, "uyelikler/info.html", {"user": request.user})