from django import forms
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        label="",
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter your username"}),
    )
    password = forms.CharField(
        max_length=150,
        label="",
        widget=forms.PasswordInput(attrs={"class": "form-control", "type": "password", "placeholder": "Enter your password"}),
    )


class SignupForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        label="",
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Choose a username"}),
    )
    password = forms.CharField(
        max_length=150,
        label="",
        widget=forms.PasswordInput(attrs={"class": "form-control", "type": "password", "placeholder": "Create a password"}),
    )
    password_confirmation = forms.CharField(
        max_length=150,
        label="",
        widget=forms.PasswordInput(attrs={"class": "form-control", "type": "password", "placeholder": "Confirm your password"}),
    )

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirmation = cleaned_data.get("password_confirmation")

        if password != password_confirmation:
            raise forms.ValidationError("The passwords do not match")

class Custom_Password_Change_Form(PasswordChangeForm):
    old_password = forms.CharField(
        max_length=150,
        label="",
        widget=forms.PasswordInput(attrs={"class": "form-control", "type": "password", "placeholder": "Current password"}),
    )
    new_password1 = forms.CharField(
        max_length=150,
        label="",
        widget=forms.PasswordInput(attrs={"class": "form-control", "type": "password", "placeholder": "New password"}),
    )
    new_password2 = forms.CharField(
        max_length=150,
        label="",
        widget=forms.PasswordInput(attrs={"class": "form-control", "type": "password", "placeholder": "Confirm new password"}),
    )
