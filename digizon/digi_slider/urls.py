# digi_slider/urls.py

from django.urls import path
from .views import index

urlpatterns = [
    path('', index, name='digi_slider_index'),  # Map the index view to the root URL
]