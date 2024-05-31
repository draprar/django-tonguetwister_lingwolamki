from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import JsonResponse
from .models import Twister, Articulator, Exercise


def main(request):
    twisters = Twister.objects.all().order_by('id')
    records = Articulator.objects.all()[:1]
    exercises = Exercise.objects.all()[:1]
    paginator = Paginator(twisters, 1)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    context = {'page_obj': page_obj,
               'records': records,
               'exercises': exercises}

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


def error_404_view(request, exception):
    data = {}
    return render(request, 'tonguetwister/404.html', data)
