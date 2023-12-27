from django.db import models
from django.contrib.auth.models import User
from races.models import Race

class Result(models.Model):
    time = models.DurationField()
    hours = models.DurationField(null=True)
    minutes = models.DurationField(null=True)
    seconds = models.DurationField(null=True)
    place = models.SmallIntegerField(null=True)
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
