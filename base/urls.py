from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tonguetwister.urls')),
]

handler404 = 'tonguetwister.views.error_404_view'
