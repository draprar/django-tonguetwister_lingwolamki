from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Twister, Articulator, Exercise, Trivia, Funfact
from .forms import ArticulatorForm, ExerciseForm, TwisterForm, TriviaForm, FunfactForm


def main(request):
    twisters = Twister.objects.all().order_by('id')
    articulators = Articulator.objects.all()[:1]
    exercises = Exercise.objects.all()[:1]
    trivia = Trivia.objects.all()[:0]
    funfacts = Funfact.objects.all()[:0]
    paginator = Paginator(twisters, 1)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    context = {'page_obj': page_obj,
               'articulators': articulators,
               'exercises': exercises,
               'trivia': trivia,
               'funfacts': funfacts,
               }

    if request.htmx:
        return render(request, 'tonguetwister/partials/gen/list.html', context)
    return render(request, 'tonguetwister/main.html', context)


def load_more_records(request):
    offset = int(request.GET.get('offset', 0))
    limit = 1
    records = Articulator.objects.all()[offset:offset + limit]
    data = list(records.values())
    return JsonResponse(data, safe=False)


def load_more_exercises(request):
    offset = int(request.GET.get('offset', 0))
    limit = 1
    exercises = Exercise.objects.all()[offset:offset + limit]
    data = list(exercises.values())
    return JsonResponse(data, safe=False)


def load_more_trivia(request):
    offset = int(request.GET.get('offset', 0))
    limit = 1
    trivia = Trivia.objects.all()[offset:offset + limit]
    data = list(trivia.values())
    return JsonResponse(data, safe=False)


def load_more_funfacts(request):
    offset = int(request.GET.get('offset', 0))
    limit = 1
    funfacts = Funfact.objects.all()[offset:offset + limit]
    data = list(funfacts.values())
    return JsonResponse(data, safe=False)


def error_404_view(request, exception):
    data = {}
    return render(request, 'tonguetwister/404.html', data)


@login_required
def articulator_list(request):
    articulators = Articulator.objects.all()
    return render(request, 'tonguetwister/articulators/articulator_list.html', {'articulators': articulators})


@login_required
def articulator_add(request):
    if request.method == "POST":
        form = ArticulatorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articulator_list')
    else:
        form = ArticulatorForm()
    return render(request, 'tonguetwister/articulators/articulator_form.html', {'form': form})


@login_required
def articulator_edit(request, pk):
    articulator = get_object_or_404(Articulator, pk=pk)
    if request.method == "POST":
        form = ArticulatorForm(request.POST, instance=articulator)
        if form.is_valid():
            form.save()
            return redirect('articulator_list')
    else:
        form = ArticulatorForm(instance=articulator)
    return render(request, 'tonguetwister/articulators/articulator_form.html', {'form': form})


@login_required
def articulator_delete(request, pk):
    articulator = get_object_or_404(Articulator, pk=pk)
    if request.method == "POST":
        articulator.delete()
        return redirect('articulator_list')
    return render(request, 'tonguetwister/articulators/articulator_confirm_delete.html', {'articulator': articulator})


@login_required
def exercise_list(request):
    exercises = Exercise.objects.all()
    return render(request, 'tonguetwister/exercises/exercise_list.html', {'exercises': exercises})


@login_required
def exercise_add(request):
    if request.method == "POST":
        form = ExerciseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('exercise_list')
    else:
        form = ExerciseForm()
    return render(request, 'tonguetwister/exercises/exercise_form.html', {'form': form})


@login_required
def exercise_edit(request, pk):
    exercise = get_object_or_404(Exercise, pk=pk)
    if request.method == "POST":
        form = ExerciseForm(request.POST, instance=exercise)
        if form.is_valid():
            form.save()
            return redirect('exercise_list')
    else:
        form = ExerciseForm(instance=exercise)
    return render(request, 'tonguetwister/exercises/exercise_form.html', {'form': form})


@login_required
def exercise_delete(request, pk):
    exercise = get_object_or_404(Exercise, pk=pk)
    if request.method == "POST":
        exercise.delete()
        return redirect('exercise_list')
    return render(request, 'tonguetwister/exercises/exercise_confirm_delete.html', {'exercise': exercise})


@login_required
def twister_list(request):
    twisters = Twister.objects.all()
    return render(request, 'tonguetwister/twisters/twister_list.html', {'twisters': twisters})


@login_required
def twister_add(request):
    if request.method == "POST":
        form = TwisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('twister_list')
    else:
        form = TwisterForm()
    return render(request, 'tonguetwister/twisters/twister_form.html', {'form': form})


@login_required
def twister_edit(request, pk):
    twister = get_object_or_404(Twister, pk=pk)
    if request.method == "POST":
        form = TwisterForm(request.POST, instance=twister)
        if form.is_valid():
            form.save()
            return redirect('twister_list')
    else:
        form = TwisterForm(instance=twister)
    return render(request, 'tonguetwister/twisters/twister_form.html', {'form': form})


@login_required
def twister_delete(request, pk):
    twister = get_object_or_404(Twister, pk=pk)
    if request.method == "POST":
        twister.delete()
        return redirect('twister_list')
    return render(request, 'tonguetwister/twisters/twister_confirm_delete.html', {'twister': twister})


@login_required
def trivia_list(request):
    trivia = Trivia.objects.all()
    return render(request, 'tonguetwister/trivia/trivia_list.html', {'trivia': trivia})


@login_required
def trivia_add(request):
    if request.method == "POST":
        form = TriviaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('trivia_list')
    else:
        form = TriviaForm()
    return render(request, 'tonguetwister/trivia/trivia_form.html', {'form': form})


@login_required
def trivia_edit(request, pk):
    trivia = get_object_or_404(Trivia, pk=pk)
    if request.method == "POST":
        form = TriviaForm(request.POST, instance=trivia)
        if form.is_valid():
            form.save()
            return redirect('trivia_list')
    else:
        form = TriviaForm(instance=trivia)
    return render(request, 'tonguetwister/trivia/trivia_form.html', {'form': form})


@login_required
def trivia_delete(request, pk):
    t = get_object_or_404(Trivia, pk=pk)
    if request.method == "POST":
        t.delete()
        return redirect('trivia_list')
    return render(request, 'tonguetwister/trivia/trivia_confirm_delete.html', {'t': t})


@login_required
def funfact_list(request):
    funfacts = Funfact.objects.all()
    return render(request, 'tonguetwister/funfacts/funfact_list.html', {'funfacts': funfacts})


@login_required
def funfact_add(request):
    if request.method == "POST":
        form = FunfactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('funfact_list')
    else:
        form = FunfactForm()
    return render(request, 'tonguetwister/funfacts/funfact_form.html', {'form': form})


@login_required
def funfact_edit(request, pk):
    funfact = get_object_or_404(Funfact, pk=pk)
    if request.method == "POST":
        form = FunfactForm(request.POST, instance=funfact)
        if form.is_valid():
            form.save()
            return redirect('funfact_list')
    else:
        form = FunfactForm(instance=funfact)
    return render(request, 'tonguetwister/funfacts/funfact_form.html', {'form': form})


@login_required
def funfact_delete(request, pk):
    funfact = get_object_or_404(Funfact, pk=pk)
    if request.method == "POST":
        funfact.delete()
        return redirect('funfact_list')
    return render(request, 'tonguetwister/funfacts/funfact_confirm_delete.html', {'funfact': funfact})
