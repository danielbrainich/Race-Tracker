from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from races.models import Race
from races.forms import AddRaceForm
from datetime import date

@login_required
def list_races(request):
    race_list = Race.objects.filter(owner=request.user)

    future_races = []
    past_races = []

    today = date.today()

    for race in race_list:
        if race.date > today:
            future_races.append(race)
        else:
            past_races.append(race)

    context = {
        "all_races": race_list,
        "future_races": future_races,
        "past_races": past_races,

    }
    return render(request, "races/race_list.html", context)

@login_required
def show_race(request, id):
    race = get_object_or_404(Race, id=id)
    context = {
        "race_object": race,
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
            return redirect("list_races")
    else:
        form = AddRaceForm()
    context = {
        "add_race_form": form,
    }
    return render(request, "races/add_race.html", context)

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
    }
    return render(request, "races/edit_race.html", context)
