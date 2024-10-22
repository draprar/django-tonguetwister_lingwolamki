from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tonguetwister.urls')),  # include URL patterns from the 'tonguetwister' app
]

# Custom error handler for 404 errors
handler404 = 'tonguetwister.views.error_404_view'
