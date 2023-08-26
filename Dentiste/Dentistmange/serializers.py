from rest_framework import serializers
from .models import Patient, Dentist, Appointment, Invoice

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

class DentistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dentist
        fields = '__all__'

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'

class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = '__all__'
