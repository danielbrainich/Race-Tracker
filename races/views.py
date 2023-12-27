from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from races.models import Race
from races.forms import AddRaceForm, AddResultToRaceForm
from datetime import date
from datetime import timedelta
from common.calculations import calculate_percentile, calculate_pace
from results.models import Result
from django.urls import reverse

@login_required
def list_races(request):
    race_list = Race.objects.filter(owner=request.user)
    future_races = []
    past_races = []
    today = date.today()

    distance_image_mapping = {
        3.1: "5k.png",
        6.2: "10k.png",
        13.1: "half.png",
        26.2: "marathon.png",
        18.6: "30k.png",
        21.7: "35k.png",
        31.1: "50k.png",
        50: "50m.png",
        62.1: "100k.png",
        100: "100m.png",
    }

    for race in race_list:
        if race.date > today:
            future_races.append(race)
        else:
            past_races.append(race)

        image_filename = distance_image_mapping.get(race.distance, "default.png")
        race.image_filename = image_filename

    context = {
        "all_races": race_list,
        "future_races": future_races,
        "past_races": past_races,
        "image_filename": image_filename,
    }
    return render(request, "races/race_list.html", context)

@login_required
def show_race(request, id):
    race = get_object_or_404(Race, id=id)
    if request.user != race.owner:
        return redirect("home")
    try:
        race_result = race.result
    except Result.DoesNotExist:
        race_result = None
    result_percentile = None
    result_pace = None
    if race_result:
        result_percentile = calculate_percentile(race_result)
        result_pace = calculate_pace(race_result)

    context = {
        "race": race,
        "result_percentile": result_percentile,
        "result_pace": result_pace,
    }
    return render(request, "races/race_details.html", context)

@login_required
def add_race(request):
    if request.method == "POST":
        form = AddRaceForm(request.POST)
        if form.is_valid():
            race = form.save(False)
            race.owner = request.user
            race.save()
            detail_url = reverse("show_race", args=[race.id])
            return redirect(detail_url)
    else:
        form = AddRaceForm()
    context = {
        "add_race_form": form,
    }
    return render(request, "races/add_race.html", context)

@login_required
def add_result_to_race(request, id):
    race = get_object_or_404(Race, id=id)

    if request.method == 'POST':
        form = AddResultToRaceForm(request.POST)
        if form.is_valid():
            result = form.save(False)
            result.race = race
            result.owner = request.user
            total_seconds = form.cleaned_data.get("hours", 0) * 3600 + \
                            form.cleaned_data.get("minutes", 0) * 60 + \
                            form.cleaned_data.get("seconds", 0)
            result.time = timedelta(seconds=total_seconds)
            result.save()
            return redirect("show_race", id=id)
    else:
        form = AddResultToRaceForm()

    context = {
        "form": form,
        "race": race,
    }

    return render(request, "races/add_result_to_race.html", context)

@login_required
def edit_race(request, id):
    race = get_object_or_404(Race, id=id)
    if request.method == "POST":
        form = AddRaceForm(request.POST, instance=race)
        if form.is_valid():
            form.save()
            return redirect("show_race", id=id)
    else:
        form = AddRaceForm(instance=race)
    context = {
        "edit_race_form": form,
        "race": race,
    }
    return render(request, "races/edit_race.html", context)

@login_required
def delete_race(request, id):
    race = get_object_or_404(Race, id=id)

    if request.method == "POST":
        race.delete()
        return redirect("home")

    context = {
        "race": race
        }

    return render(request, "races/delete_race.html", context)
