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
            "overall_place",
            "division",
            "division_place",
            "finishers",
            "link",
        ]

        widgets = {
            "race": forms.Select(attrs={"class": "form-control"}),
            "time": forms.NumberInput(attrs={"class": "form-control", "placeholder": "hh:mm:ss"}),
            "overall_place": forms.NumberInput(attrs={"class": "form-control"}),
            "division": forms.Select(attrs={"class": "form-control"}),
            "division_place": forms.NumberInput(attrs={"class": "form-control"}),
            "finishers": forms.NumberInput(attrs={"class": "form-control"}),
            "link": forms.URLInput(attrs={"class": "form-control", "placeholder": "http://www.myrace.com"}),
        }
