from django.contrib import admin
from races.models import Race

@admin.register(Race)
class RaceAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "distance",
        "location",
        "terrain",
        "elevation_gain",
        "date",
        "id",
        ]
