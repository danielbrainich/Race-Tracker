from django.db import models
from django.contrib.auth.models import User
from races.models import Race

DIVISION_CHOICES = [
    ("m", "M"),
    ("f", "F"),
]

class Result(models.Model):
    time = models.DurationField()
    overall_place = models.SmallIntegerField()
    division = models.CharField(
        max_length=1,
        choices=DIVISION_CHOICES,
    )
    division_place = models.SmallIntegerField()
    finishers = models.SmallIntegerField()
    link = models.URLField(null=True)
    race = models.OneToOneField(
        Race,
        related_name="result",
        on_delete=models.CASCADE,
    )
    owner = models.ForeignKey(
        User,
        related_name="result",
        on_delete=models.CASCADE,
    )
