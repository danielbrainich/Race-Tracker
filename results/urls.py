from django.urls import path
from results.views import add_result, list_results

urlpatterns = [
    path("", list_results, name="list_results"),
    path("add/", add_result, name="add_result"),

]
