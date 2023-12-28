from django.forms import ModelForm
from results.models import Result
from django import forms
from datetime import timedelta


class AddResultForm(ModelForm):
    hours = forms.IntegerField(
        min_value=0,
        max_value=99,
        widget=forms.NumberInput(attrs={"class": "form-control"}),
    )
    minutes = forms.IntegerField(
        min_value=0,
        max_value=59,
        widget=forms.NumberInput(attrs={"class": "form-control"}),
    )
    seconds = forms.IntegerField(
        min_value=0,
        max_value=59,
        widget=forms.NumberInput(attrs={"class": "form-control"}),
    )

    class Meta:
        model = Result

        fields = [
            "race",
            "place",
            "finishers",
            "hours",
            "minutes",
            "seconds",
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
