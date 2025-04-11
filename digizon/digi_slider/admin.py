# digi_slider/admin.py

from django.contrib import admin
from .models import DigiSlider, DeviceInfo

@admin.register(DeviceInfo)
class DeviceInfoAdmin(admin.ModelAdmin):
    list_display = ('department', 'building', 'device', 'shift')  # Display these fields in the admin

@admin.register(DigiSlider)
class DigiSliderAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'background_color', 'text_color', 'device_type', 'device_info')  # Display these fields in the admin
    list_filter = ('device_type', 'device_info__department', 'device_info__building')  # Add filters by device type, department, and building