from django.urls import path
from . import views


urlpatterns = [
    path('', views.main, name='main'),
    path('load-more-records/', views.load_more_records, name='load_more_records'),
    path('load-more-exercises/', views.load_more_exercises, name='load_more_exercises'),
]
