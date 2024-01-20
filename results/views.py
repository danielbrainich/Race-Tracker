from django.shortcuts import render, redirect, get_object_or_404
from results.models import Result
from races.models import Race
from results.forms import AddResultForm
from races.forms import AddResultToRaceForm
from django.contrib.auth.decorators import login_required
from datetime import timedelta
from common.calculations import calculate_percentile, calculate_pace


def add_result(request):
    races = Race.objects.filter(owner=request.user, result=None)
    if request.method == "POST":
        form = AddResultForm(request.POST)
        if form.is_valid():
            result = form.save(commit=False)
            result.owner = request.user
            total_seconds = (
                form.cleaned_data.get("hours", 0) * 3600
                + form.cleaned_data.get("minutes", 0) * 60
                + form.cleaned_data.get("seconds", 0)
            )
            result.time = timedelta(seconds=total_seconds)
            result.save()
            return redirect("list_results")
    else:
        form = AddResultForm()
        form.fields["race"].queryset = Race.objects.filter(
            owner=request.user, result=None
        )

    context = {
        "form": form,
        "races": races,
    }

    return render(request, "results/add_result.html", context)


@login_required
def list_results(request):
    results = Result.objects.filter(owner=request.user)
    result_list = [
        {
            "result": result,
            "percentile": calculate_percentile(result),
            "pace": calculate_pace(result),
        }
        for result in results
    ]

    context = {"result_list": result_list}
    return render(request, "results/result_list.html", context)


def edit_result(request, race_id, result_id):
    race = get_object_or_404(Race, id=race_id)
    result = get_object_or_404(Result, id=result_id, race=race)

    if request.method == "POST":
        form = AddResultToRaceForm(request.POST, instance=result)
        if form.is_valid():
            cleaned_time = form.clean_time()
            result.time = cleaned_time
            result.save()
            return redirect("show_race", id=race_id)
    else:
        form = AddResultToRaceForm(instance=result)

    context = {
        "form": form,
        "race": race,
    }

    return render(request, "results/edit_result.html", context)


@login_required
def delete_result(request, race_id, result_id):
    race = get_object_or_404(Race, id=race_id)
    result = get_object_or_404(Result, id=result_id, race=race)

    if request.method == "POST":
        result.delete()
        return redirect("show_race", id=race_id)

    context = {"race": race}

    return render(request, "results/delete_result.html", context)
