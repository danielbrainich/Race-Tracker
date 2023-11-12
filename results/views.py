from django.shortcuts import render, redirect, get_object_or_404
from results.models import Result
# from races.models import Race
from results.forms import AddResultForm
from django.contrib.auth.decorators import login_required


@login_required
def add_result(request):
    if request.method == "POST":
        form = AddResultForm(request.POST)
        if form.is_valid():
            result = form.save(False)
            result.owner = request.user
            result.save()
            return redirect("list_results")
    else:
        form = AddResultForm()
    context = {
        "add_result_form": form,
    }
    return render(request, "results/add_result.html", context)


@login_required
def list_results(request):
    result = Result.objects.filter(owner=request.user)
    context = {"result_list": result}
    return render(request, "results/result_list.html", context)

@login_required
def edit_result(request, id):
    race = get_object_or_404(Race, id=id)
    result =race.result

    if request.method == "POST":
        form = EditResultForm(request.POST, instance=result)
        if form.is_valid():
            form.save()
            return redirect("list_results", id=id)
    else:
        form = AddResultForm(instance=result)
    context = {
        "edit_result_form": form,
    }
    return render(request, "results/edit_result.html", context)
