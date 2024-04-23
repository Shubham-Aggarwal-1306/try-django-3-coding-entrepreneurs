from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Create your views here.
def login_view(request):
    form = None
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("/")
    else:
        form = AuthenticationForm(request)
    context = {
        "form": form
    }
    return render(request, "accounts/login.html", context=context)

def register_view(request):
    form = UserCreationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("/login")
    context = {
        "form": form
    }
    return render(request, "accounts/register.html", context=context)

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("/login")
    
    return render(request, "accounts/logout.html", context={})