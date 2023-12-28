from django.forms import ModelForm, IntegerField
from races.models import Race
from results.models import Result
from django import forms
from datetime import timedelta


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

        labels = {"elevation_gain": "Ft. Elev. Gain"}

        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": ""}),
            "distance": forms.Select(
                attrs={"class": "form-control", "placeholder": ""}
            ),
            "location": forms.TextInput(
                attrs={"class": "form-control", "placeholder": ""}
            ),
            "terrain": forms.Select(attrs={"class": "form-control", "placeholder": ""}),
            "elevation_gain": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": ""}
            ),
            "date": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
            "link": forms.URLInput(attrs={"class": "form-control", "placeholder": ""}),
        }


class AddResultToRaceForm(ModelForm):
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
            "place",
            "finishers",
            "hours",
            "minutes",
            "seconds",
            "link",
        ]

        widgets = {
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
