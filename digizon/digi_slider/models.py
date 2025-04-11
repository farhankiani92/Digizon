# digi_slider/models.py

from django.db import models

class DeviceInfo(models.Model):
    department = models.CharField(max_length=100)  # Department name
    building = models.CharField(max_length=100)  # Building name
    device = models.CharField(max_length=100)  # Device name
    shift = models.CharField(max_length=100)  # Shift name

    def __str__(self):
        return f"{self.department} - {self.building} - {self.device} - {self.shift}"  # String representation

class DigiSlider(models.Model):
    DEVICE_CHOICES = [
        ('TV', 'TV'),
        ('desktop', 'Desktop'),
        ('tablet', 'Tablet'),
        ('mobile', 'Mobile'),
    ]

    title = models.CharField(max_length=100)  # Title of the slider
    image = models.ImageField(upload_to='slider_images/')  # Image for the slider
    background_color = models.CharField(max_length=7)  # Background color in hex
    text_color = models.CharField(max_length=7)  # Text color in hex
    device_type = models.CharField(max_length=10, choices=DEVICE_CHOICES, null=True, blank=True, default='TV')  # Default
    device_info = models.ForeignKey(DeviceInfo, on_delete=models.CASCADE, null=True, blank=True, related_name='sliders')  # Link to DeviceInfo

    def __str__(self):
        return f"{self.title} ({self.device_type})"  # Return title and device type