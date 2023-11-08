from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from accounts.forms import LoginForm, SignupForm


def account_login(request):
    if request.method == "POST":
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data["username"]
            password = login_form.cleaned_data["password"]
            user = authenticate(
                request,
                username=username,
                password=password,
            )
            if user is not None:
                login(request, user)
                return redirect("home")
    else:
        login_form = LoginForm()
    context = {
        "login_form": login_form,
    }
    return render(request, "accounts/login.html", context)


def account_logout(request):
    logout(request)
    return redirect("login")


def account_signup(request):
    if request.method == "POST":
        signup_form = SignupForm(request.POST)
        if signup_form.is_valid():
            username = signup_form.cleaned_data["username"]
            password = signup_form.cleaned_data["password"]
            password_confirmation = signup_form.cleaned_data[
                "password_confirmation"
            ]

            if password == password_confirmation:
                user = User.objects.create_user(username, password=password)

                login(request, user)
                return redirect("list_projects")
            else:
                signup_form.add_error("password", "the passwords do not match")
    else:
        signup_form = SignupForm()
    context = {
        "signup_form": signup_form,
    }
    return render(request, "accounts/signup.html", context)

