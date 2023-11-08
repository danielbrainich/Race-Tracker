# Generated by Django 4.2.7 on 2023-11-08 20:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('races', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DurationField()),
                ('overall_place', models.SmallIntegerField()),
                ('division', models.CharField(choices=[('m', 'M'), ('f', 'F')], max_length=1)),
                ('division_place', models.SmallIntegerField()),
                ('finishers', models.SmallIntegerField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='results', to=settings.AUTH_USER_MODEL)),
                ('race', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='results', to='races.race')),
            ],
        ),
    ]
