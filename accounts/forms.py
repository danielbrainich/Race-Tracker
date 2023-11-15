from django import forms
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    password = forms.CharField(
        max_length=150,
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
    )


class SignupForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    password = forms.CharField(
        max_length=150,
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
    )
    password_confirmation = forms.CharField(
        max_length=150,
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
    )


class Custom_Password_Change_Form(PasswordChangeForm):
    old_password = forms.CharField(
        max_length=150,
        widget=forms.PasswordInput(attrs={"class": "form-control", "type": "password"}),
    )
    new_password1 = forms.CharField(
        max_length=150,
        widget=forms.PasswordInput(attrs={"class": "form-control", "type": "password"}),
    )
    new_password2 = forms.CharField(
        max_length=150,
        widget=forms.PasswordInput(attrs={"class": "form-control", "type": "password"}),
    )
    class Meta:
        model = User
        fields = [
            "old_passsword",
            "new_password1",
            "new_password2"
            ]
