from django.shortcuts import render
from .models import Apparatus, Articulation, Twister


def main(request):
    myset = {
        "apparatus": Apparatus.objects.all()[0:1],
        "apparatus_next": Apparatus.objects.all()[1:3],
        "articulation": Articulation.objects.all(),
        "twister": Twister.objects.all(),
    }
    return render(request, 'tonguetwister/main.html', myset)


def error_404_view(request, exception):
    data = {}
    return render(request, 'tonguetwister/404.html', data)
