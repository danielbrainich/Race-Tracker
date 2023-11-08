from django.db import models
from django.contrib.auth.models import User
from races.models import Race

class Result(models.Model):
    time = models.IntegerField()
    overall_place = models.IntegerField()
    division = models.CharField(max_length=1)
    division_place = models.IntegerField()
    finishers = models.IntegerField()
    race = models.ForeignKey(
        Race,
        related_name="results",
        on_delete=models.CASCADE,
        null=True
    )
    owner = models.ForeignKey(
        User,
        related_name="results",
        on_delete=models.CASCADE,
        null=True,
    )
