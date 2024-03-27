from django.db import models
from patient_service.models import Patient  # Assuming you have a Patient model

class Billing(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Paid', 'Paid')])
    payment_method = models.CharField(max_length=50, blank=True, null=True)
    invoice_number = models.CharField(max_length=50, unique=True)
    comments = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Bill for {self.patient.first_name} {self.patient.last_name} - Invoice #{self.invoice_number}"
