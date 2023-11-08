from django.urls import path
from races.views import list_races, show_race, add_race

urlpatterns = [
    path("", list_races, name="list_races"),
    path("<int:id>", show_race, name="show_race"),
    path("add", add_race, name="add_race"),
]
