from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect



# Create your views here.
def login_route(request):
    if request.method == "GET":
        return render(request, "auth/login.html")

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return render(request, "auth/login.html", {"error": "Invalid Username"})

        if not user.check_password(password):
            return render(request, "auth/login.html", {"error": "Invalid Password"})

        login(request, user)

        return redirect("/", permanent=True)


def register_route(request):
    if request.method == "GET":
        return redirect("/login", permanent=True)

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if password != confirm_password:
            return render(request, "auth/login.html", {"error": "Passwords do not match"})

        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            user = User.objects.create_user(username=username, password=password)
            user.first_name = request.POST.get("name")
            user.email = request.POST.get("email")

            user.save()
            login(request, user)
            return redirect("/", permanent=True)

        return render(request, "auth/login.html", {"error": "User already exists"})


@login_required(login_url='/auth/login')
def logout_route(request):
    logout(request)
    return redirect("/", permanent=True)
