from django.forms import ModelForm
from races.models import Race
from results.models import Result
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
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": ""}),
            "distance": forms.Select(attrs={"class": "form-control", "placeholder": ""}),
            "location": forms.TextInput(attrs={"class": "form-control", "placeholder": "City, State"}),
            "terrain": forms.Select(attrs={"class": "form-control", "placeholder": "Terrain"}),
            "elevation_gain": forms.NumberInput(attrs={"class": "form-control", "placeholder": "In feet"}),
            "date": forms.DateInput(attrs={"class": "form-control", "placeholder": "mm/dd/yyyy"}),
            "link": forms.URLInput(attrs={"class": "form-control", "placeholder": "https://www.myrace.com"}),
        }

class AddResultToRaceForm(ModelForm):

    class Meta:
        model = Result

        fields = [
            "time",
            "place",
            "finishers",
            "link",
        ]

        widgets = {
            "time": forms.NumberInput(attrs={"class": "form-control", "placeholder": "hhmmss"}),
            "place": forms.NumberInput(attrs={"class": "form-control"}),
            "finishers": forms.NumberInput(attrs={"class": "form-control"}),
            "link": forms.URLInput(attrs={"class": "form-control", "placeholder": "https://www.myrace.com"}),
        }
