from django.urls import path, include
from . import views
from .views import login_view, register_view, activate
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.main, name='main'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('activate/<uidb64>/<token>/', activate, name='activate'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('load-more-articulators/', views.load_more_articulators, name='load_more_articulators'),
    path('load-more-exercises/', views.load_more_exercises, name='load_more_exercises'),
    path('load-more-twisters/', views.load_more_twisters, name='load_more_twisters'),
    path('load-more-trivia/', views.load_more_trivia, name='load_more_trivia'),
    path('load-more-funfacts/', views.load_more_funfacts, name='load_more_funfacts'),
    path('articulators/', views.articulator_list, name='articulator_list'),
    path('articulators/add/', views.articulator_add, name='articulator_add'),
    path('articulators/<int:pk>/edit/', views.articulator_edit, name='articulator_edit'),
    path('articulators/<int:pk>/delete/', views.articulator_delete, name='articulator_delete'),
    path('exercises/', views.exercise_list, name='exercise_list'),
    path('exercises/add/', views.exercise_add, name='exercise_add'),
    path('exercises/<int:pk>/edit/', views.exercise_edit, name='exercise_edit'),
    path('exercises/<int:pk>/delete/', views.exercise_delete, name='exercise_delete'),
    path('twisters/', views.twister_list, name='twister_list'),
    path('twisters/add/', views.twister_add, name='twister_add'),
    path('twisters/<int:pk>/edit/', views.twister_edit, name='twister_edit'),
    path('twisters/<int:pk>/delete/', views.twister_delete, name='twister_delete'),
    path('trivia/', views.trivia_list, name='trivia_list'),
    path('trivia/add/', views.trivia_add, name='trivia_add'),
    path('trivia/<int:pk>/edit/', views.trivia_edit, name='trivia_edit'),
    path('trivia/<int:pk>/delete/', views.trivia_delete, name='trivia_delete'),
    path('funfacts/', views.funfact_list, name='funfact_list'),
    path('funfacts/add/', views.funfact_add, name='funfact_add'),
    path('funfacts/<int:pk>/edit/', views.funfact_edit, name='funfact_edit'),
    path('funfacts/<int:pk>/delete/', views.funfact_delete, name='funfact_delete'),
    path('oldpolishs/', views.oldpolish_list, name='oldpolish_list'),
    path('oldpolishs/add/', views.oldpolish_add, name='oldpolish_add'),
    path('oldpolishs/<int:pk>/edit/', views.oldpolish_edit, name='oldpolish_edit'),
    path('oldpolishs/<int:pk>/delete/', views.oldpolish_delete, name='oldpolish_delete'),
    path('user-content/', views.user_content, name='user_content'),
    path('add-articulator/<int:articulator_id>/', views.add_articulator, name='add_articulator'),
    path('delete-articulator/<int:articulator_id>/', views.delete_articulator, name='delete_articulator'),
    path('add-exercise/<int:exercise_id>/', views.add_exercise, name='add_exercise'),
    path('delete-exercise/<int:exercise_id>/', views.delete_exercise, name='delete_exercise'),
    path('add-twister/<int:twister_id>/', views.add_twister, name='add_twister'),
    path('delete-twister/<int:twister_id>/', views.delete_twister, name='delete_twister'),
    path('contact/', views.contact, name='contact'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
