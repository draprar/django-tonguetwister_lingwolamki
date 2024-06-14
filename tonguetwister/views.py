from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.http import JsonResponse
from .models import Twister, Articulator, Exercise, Trivia, Funfact
from .forms import ArticulatorForm, ExerciseForm, TwisterForm, TriviaForm, FunfactForm


def main(request):
    twisters = Twister.objects.all().order_by('id')
    records = Articulator.objects.all()[:1]
    exercises = Exercise.objects.all()[:1]
    trivia = Trivia.objects.all()[:0]
    funfacts = Funfact.objects.all()[:0]
    paginator = Paginator(twisters, 1)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    context = {'page_obj': page_obj,
               'records': records,
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


def add_articulator(request):
    if request.method == 'POST':
        form = ArticulatorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ArticulatorForm()
    return render(request, 'tonguetwister/forms/add_articulator.html', {'form': form})


def add_exercise(request):
    if request.method == 'POST':
        form = ExerciseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ExerciseForm()
    return render(request, 'tonguetwister/forms/add_exercise.html', {'form': form})


def add_twister(request):
    if request.method == 'POST':
        form = TwisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = TwisterForm()
    return render(request, 'tonguetwister/forms/add_twister.html', {'form': form})


def add_trivia(request):
    if request.method == 'POST':
        form = TriviaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = TriviaForm()
    return render(request, 'tonguetwister/forms/add_trivia.html', {'form': form})


def add_funfact(request):
    if request.method == 'POST':
        form = FunfactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = FunfactForm()
    return render(request, 'tonguetwister/forms/add_funfact.html', {'form': form})


def success(request):
    return render(request, 'tonguetwister/forms/success.html')
