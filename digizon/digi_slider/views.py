# digi_slider/views.py

from django.shortcuts import render
from .models import DigiSlider

def index(request):
    sliders = DigiSlider.objects.all()  # Fetch all sliders from the database
    return render(request, 'digi_slider/index.html', {'sliders': sliders})  # Render the index template with sliders