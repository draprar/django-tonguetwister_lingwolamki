from django.urls import path
from . import views


urlpatterns = [
    path('', views.main, name='main'),
    path('load-more-records/', views.load_more_records, name='load_more_records'),
    path('load-more-exercises/', views.load_more_exercises, name='load_more_exercises'),
    path('load-more-trivia/', views.load_more_trivia, name='load_more_trivia'),
    path('load-more-funfacts/', views.load_more_funfacts, name='load_more_funfacts'),
]
