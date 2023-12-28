from django.db import models
from django.contrib.auth.models import User
from races.models import Race


class Result(models.Model):
    time = models.DurationField(null=True)
    place = models.SmallIntegerField(null=True)
    finishers = models.SmallIntegerField(null=True)
    link = models.URLField(null=True, blank=True)
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
