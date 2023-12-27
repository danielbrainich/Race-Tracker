from django.shortcuts import render, redirect, get_object_or_404
from results.models import Result
from races.models import Race
from results.forms import AddResultForm
from django.contrib.auth.decorators import login_required
from datetime import timedelta
from common.calculations import calculate_percentile, calculate_pace

def add_result(request):
    if request.method == "POST":
        form = AddResultForm(request.POST)
        if form.is_valid():
            result = form.save(commit=False)
            result.owner = request.user
            total_seconds = form.cleaned_data.get("hours", 0) * 3600 + \
                            form.cleaned_data.get("minutes", 0) * 60 + \
                            form.cleaned_data.get("seconds", 0)
            result.time = timedelta(seconds=total_seconds)

            result.save()
            return redirect("home")
    else:
        form = AddResultForm()
        form.fields["race"].queryset = Race.objects.filter(owner=request.user, result=None)

    context = {
        "add_result_form": form,
    }
    return render(request, "results/add_result.html", context)


@login_required
def list_results(request):
    results = Result.objects.filter(owner=request.user)

    result_list = []
    for result in results:
        result_percentile = calculate_percentile(result)
        result_pace = calculate_pace(result)
        result_list.append({
            "result": result,
            "percentile": result_percentile,
            "pace": result_pace
        })

    context = {"result_list": result_list}
    return render(request, "results/result_list.html", context)

@login_required
def edit_result(request, race_id, result_id):
    race_instance = get_object_or_404(Race, id=race_id)
    result_instance = get_object_or_404(Result, id=result_id, race=race_instance)

    if request.method == "POST":
        form = AddResultForm(request.POST, instance=result_instance)
        if form.is_valid():
            form.save()
            return redirect("show_race", id=race_id)
    else:
        form = AddResultForm(instance=result_instance)

    context = {
        "edit_result_form": form,
        "race": race_instance,

    }
    return render(request, "results/edit_result.html", context)

@login_required
def delete_result(request, race_id, result_id):
    race_instance = get_object_or_404(Race, id=race_id)
    result_instance = get_object_or_404(Result, id=result_id, race=race_instance)

    if request.method == "POST":
        result_instance.delete()
        return redirect("show_race", id=race_id)

    context = {
        "race": race_instance
    }

    return render(request, "results/delete_result.html", context)
