# Generated by Django 4.2.7 on 2024-01-20 17:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("races", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Result",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("time", models.DurationField(null=True)),
                ("place", models.SmallIntegerField(null=True)),
                ("finishers", models.SmallIntegerField(null=True)),
                ("link", models.URLField(blank=True, null=True)),
                (
                    "owner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="result",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "race",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="result",
                        to="races.race",
                    ),
                ),
            ],
        ),
    ]
