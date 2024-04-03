from django.urls import path
from . import views


urlpatterns = [
    path('', views.apparatus_list, name='apparatus_list'),
    path('', views.articulation_list, name='articulation_list'),
    path('', views.twister_list, name='twister_list'),
]
