from django.forms import ModelForm
from races.models import Race
from django import forms


class AddRaceForm(ModelForm):
    class Meta:
        model = Race

        fields = [
            "name",
            "distance",
            "location",
            "terrain",
            "elevation_gain",
            "date",
            "link",
        ]

        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "distance": forms.Select(attrs={"class": "form-control"}),
            "location": forms.TextInput(attrs={"class": "form-control"}),
            "terrain": forms.Select(attrs={"class": "form-control"}),
            "elevation_gain": forms.NumberInput(attrs={"class": "form-control"}),
            "date": forms.DateInput(attrs={"class": "form-control"}),
            "link": forms.URLInput(attrs={"class": "form-control"}),
        }
