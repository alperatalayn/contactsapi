from django.urls import path, include
from django.contrib import admin

# Serializers define the API representation.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]