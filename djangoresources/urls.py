"""
URL configuration for djangoresources project.
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    #   faq app
    path('resources/', include('resources.urls', namespace='resources')),
    #   index of site - no page so we send to resources home
    path('', include('resources.urls', namespace='project_home')),
]
