from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            redirect("/")
        else:
            return render(request, "accounts/login.html", context={"error": "Invalid username or password."})
    return render(request, "accounts/login.html", context={})

def register_view(request):
    return render(request, "accounts/register.html", context={})

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("/login")
    
    return render(request, "accounts/logout.html", context={})