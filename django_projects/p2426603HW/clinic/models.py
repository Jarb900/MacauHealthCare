from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.user.username)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.user.username

    def is_doctor(self):
        return hasattr(self, 'doctor')

    User.add_to_class('is_doctor', is_doctor)

class Patient(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


    def is_patient(self):
        return hasattr(self, 'patient')

    User.add_to_class('is_patient', is_patient)

class Appointment(models.Model):
    appointID = models.AutoField(primary_key=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateField()
    time = models.CharField(max_length=5)

    STATUS = (
        ('a', 'Available'),
        ('t', 'Taken'),
        ('d', 'Done'),
    )

    status = models.CharField(max_length=1, choices=STATUS, blank=True, default='a')

    def __str__(self):
        return f"Appointment {self.appointID} - {self.get_status_display()}"
