from django.utils import timezone
from django.shortcuts import render
from .models import Apparatus, Articulation, Twister
from django.http import HttpResponse
from django.template import loader

def apparatus_list(request):
    apparatuss = Apparatus.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'tonguetwister/apparatus_list.html', {'apparatuss': apparatuss})


def articulation_list(request):
    articulations = Articulation.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'tonguetwister/articulation_list.html', {'articulations': articulations})


def twister_list(request):
    twisters = Twister.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'tonguetwister/twister_list.html', {'twisters': twisters})


def error_404_view(request, exception):
    data = {}
    return render(request, 'tonguetwister/404.html', data)


def main(request):
  template = loader.get_template('tonguetwister/main.html')
  return HttpResponse(template.render())
