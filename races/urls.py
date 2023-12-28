from django.urls import path
from races.views import (
    list_races,
    show_race,
    add_race,
    edit_race,
    delete_race,
    add_result_to_race,
)

urlpatterns = [
    path("", list_races, name="list_races"),
    path("<int:id>/", show_race, name="show_race"),
    path("add/", add_race, name="add_race"),
    path("<int:id>/add_result/", add_result_to_race, name="add_result_to_race"),
    path("<int:id>/edit/", edit_race, name="edit_race"),
    path("<int:id>/delete/", delete_race, name="delete_race"),
]
