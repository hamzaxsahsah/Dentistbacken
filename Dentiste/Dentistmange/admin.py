from django.contrib import admin
from .models import Patient, Dentist, Appointment, Invoice

admin.site.register(Patient)
admin.site.register(Dentist)
admin.site.register(Appointment)
admin.site.register(Invoice)
# Register your models here.
