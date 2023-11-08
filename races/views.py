from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from races.models import Race
from races.forms import AddRaceForm

@login_required
def list_races(request):
    list = Race.objects.filter(owner=request.user)
    context = {
        "race_list": list,
    }
    return render(request, "races/list.html", context)

@login_required
def show_race(request, id):
    race = get_object_or_404(Race, id=id)
    context = {
        "race_object": race,
    }
    return render(request, "races/details.html", context)


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
