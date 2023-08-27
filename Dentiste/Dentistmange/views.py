from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Patient, Dentist, Appointment, Invoice
from .serializers import PatientSerializer, DentistSerializer, AppointmentSerializer, InvoiceSerializer

class PatientViewSet(viewsets.ModelViewSet):
    
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class DentistViewSet(viewsets.ModelViewSet):
    queryset = Dentist.objects.all()
    serializer_class = DentistSerializer

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
