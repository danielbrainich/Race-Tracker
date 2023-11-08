from django.db import models
from django.contrib.auth.models import User

class Race(models.Model):
    name = models.CharField(max_length=150)
    distance = models.CharField(max_length=150)
    location = models.CharField(max_length=150)
    terrain = models.CharField(max_length=150)
    elevation_gain = models.IntegerField()
    date = models.DateTimeField()
    owner = models.ForeignKey(
        User,
        related_name="projects",
        on_delete=models.CASCADE,
        null=True,
    )

    def __str__(self):
        return self.name
