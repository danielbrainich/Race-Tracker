from django.db import models
from django.contrib.auth.models import User


class Race(models.Model):
    DISTANCE_CHOICES = [
        ("5k", "5k"),
        ("10k", "10k"),
        ("half_marathon", "Half Marathon"),
        ("marathon", "Marathon"),
        ("30k", "30k"),
        ("35k", "35k"),
        ("50k", "50k"),
        ("50_mile", "50 mile"),
        ("100k", "100k"),
        ("100_mile", "100 mile"),
    ]
    TERRAIN_CHOICES = [
        ("trail", "Trail"),
        ("road", "Road"),
    ]

    name = models.CharField(max_length=150,
        help_text = "first last",
    )

    distance = models.CharField(
        max_length=13,
        choices=DISTANCE_CHOICES,
    )

    location = models.CharField(max_length=150,
        help_text = "city, state",
    )
    terrain = models.CharField(
        max_length=5,
        choices=TERRAIN_CHOICES,
    )
    elevation_gain = models.PositiveIntegerField(
        help_text = "in feet"
    )
    date = models.DateField(
        help_text = "mm/dd/yyyy"
    )

    link = models.URLField(null=True,
        help_text = "www.website.com"
    )


    owner = models.ForeignKey(
        User,
        related_name="projects",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name
