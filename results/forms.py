from django.forms import ModelForm
from races.models import Race
from results.models import Result
from django import forms


class AddResultForm(ModelForm):

    class Meta:
        model = Result

        fields = [
            "race",
            "time",
            "place",
            "finishers",
            "link",
        ]

        widgets = {
            "race": forms.Select(attrs={"class": "form-control"}),
            "time": forms.NumberInput(attrs={"class": "form-control", "placeholder": "hhmmss"}),
            "place": forms.NumberInput(attrs={"class": "form-control"}),
            "finishers": forms.NumberInput(attrs={"class": "form-control"}),
            "link": forms.URLInput(attrs={"class": "form-control", "placeholder": "https://www.myrace.com"}),
        }
