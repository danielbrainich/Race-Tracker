from django.urls import path
from results.views import list_results, edit_result, delete_result, add_result

urlpatterns = [
    path("", list_results, name="list_results"),
    path("add/", add_result, name="add_result"),
    path("<int:race_id>/<int:result_id>/edit", edit_result, name="edit_result"),
    path("<int:race_id>/<int:result_id>/delete", delete_result, name="delete_result")
]
