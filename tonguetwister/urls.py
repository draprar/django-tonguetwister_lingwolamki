from django.urls import path
from . import views


urlpatterns = [
    path('', views.main, name='main'),
    path('load-more-records/', views.load_more_records, name='load_more_records'),
    path('load-more-exercises/', views.load_more_exercises, name='load_more_exercises'),
    path('load-more-trivia/', views.load_more_trivia, name='load_more_trivia'),
    path('load-more-funfacts/', views.load_more_funfacts, name='load_more_funfacts'),
    path('add_articulator/', views.add_articulator, name='add_articulator'),
    path('add_exercise/', views.add_exercise, name='add_exercise'),
    path('add_twister/', views.add_twister, name='add_twister'),
    path('add_trivia/', views.add_trivia, name='add_trivia'),
    path('add_bonus/', views.add_funfact, name='add_funfact'),
    path('success/', views.success, name='success'),
]
