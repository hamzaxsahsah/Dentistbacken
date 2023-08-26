from django.db import models

class Patient(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Dentist(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    dentist = models.ForeignKey(Dentist, on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    purpose = models.TextField()

    def __str__(self):
        return f"Appointment for {self.patient} with {self.dentist}"

class Invoice(models.Model):
    appointment = models.OneToOneField(Appointment, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status_choices = [
        ('PAID', 'Paid'),
        ('UNPAID', 'Unpaid'),
    ]
    status = models.CharField(max_length=10, choices=status_choices, default='UNPAID')

    def __str__(self):
        return f"Invoice for {self.appointment}"
