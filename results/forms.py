from django.forms import ModelForm
from results.models import Result


class AddResultForm(ModelForm):
    class Meta:
        model = Result
        fields = [
            "time",
            "overall_place",
            "division",
            "division_place",
            "finishers",
            "race",
        ]
