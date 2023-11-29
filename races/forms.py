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
            "overall_place",
            "division",
            "division_place",
            "finishers",
            "link",
        ]

        widgets = {
            "time": forms.NumberInput(attrs={"class": "form-control", "placeholder": "hhmmss"}),
            "overall_place": forms.NumberInput(attrs={"class": "form-control"}),
            "division": forms.Select(attrs={"class": "form-control"}),
            "division_place": forms.NumberInput(attrs={"class": "form-control"}),
            "finishers": forms.NumberInput(attrs={"class": "form-control"}),
            "link": forms.URLInput(attrs={"class": "form-control", "placeholder": "https://www.myrace.com"}),
        }
