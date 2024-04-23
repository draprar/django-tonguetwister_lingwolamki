from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Twister


def main(request):
    twisters = Twister.objects.all().order_by('id')
    paginator = Paginator(twisters, 1)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    context = {'page_obj': page_obj}

    if request.htmx:
        return render(request, 'tonguetwister/partials/gen/list.html', context)
    return render(request, 'tonguetwister/main.html', context)


def error_404_view(request, exception):
    data = {}
    return render(request, 'tonguetwister/404.html', data)
