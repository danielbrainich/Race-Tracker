from django.urls import path
from accounts.views import account_login, account_logout, account_signup

urlpatterns = [
    path("login/", account_login, name="login"),
    path("logout/", account_logout, name="logout"),
    path("signup/", account_signup, name="signup"),
]
