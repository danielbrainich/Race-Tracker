from django.forms import ModelForm
from races.models import Race


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
