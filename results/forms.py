from django.forms import ModelForm
from results.models import Result
from django import forms
from datetime import timedelta

class AddResultForm(ModelForm):
    hours = forms.IntegerField(min_value=0, max_value=99, required=False)
    minutes = forms.IntegerField(min_value=0, max_value=59, required=False)
    seconds = forms.IntegerField(min_value=0, max_value=59, required=False)

    class Meta:
        model = Result

        fields = [
            "race",
            "place",
            "finishers",
            "link",
        ]

        widgets = {
            "race": forms.Select(attrs={"class": "form-control"}),
            "place": forms.NumberInput(attrs={"class": "form-control"}),
            "finishers": forms.NumberInput(attrs={"class": "form-control"}),
            "link": forms.URLInput(attrs={"class": "form-control", "placeholder": ""}),
        }

    def clean_time(self):
        hours = self.cleaned_data.get("hours", 0)
        minutes = self.cleaned_data.get("minutes", 0)
        seconds = self.cleaned_data.get("seconds", 0)

        time_duration = timedelta(hours=hours, minutes=minutes, seconds=seconds)
        return time_duration
