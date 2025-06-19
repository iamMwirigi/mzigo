# mzigo/urls.py

from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the Mzigo API!")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  # Include API app URLs
    path('', home),  # root path
]