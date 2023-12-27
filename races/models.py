from django.db import models
from django.contrib.auth.models import User

class Race(models.Model):
    DISTANCE_CHOICES = [
        (3.1, "5k"),
        (6.2, "10k"),
        (13.1, "Half marathon"),
        (26.2, "Marathon"),
        (18.6, "30k"),
        (21.7, "35k"),
        (31.1, "50k"),
        (50, "50 mile"),
        (62.1, "100k"),
        (100, "100 mile"),
    ]

    TERRAIN_CHOICES = [
        ("trail", "Trail"),
        ("road", "Road"),
    ]

    name = models.CharField(max_length=150)
    distance = models.FloatField(
        choices=DISTANCE_CHOICES,
    )
    location = models.CharField(max_length=150)
    terrain = models.CharField(
        max_length=5,
        choices=TERRAIN_CHOICES,
    )
    elevation_gain = models.PositiveIntegerField()
    date = models.DateField()
    link = models.URLField(null=True, blank=True)
    owner = models.ForeignKey(
        User,
        related_name="projects",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name

    def get_distance_display(self):
        for choice in self.DISTANCE_CHOICES:
            if choice[0] == self.distance:
                return choice[1]
        return None
