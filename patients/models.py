from django.db import models

# Create your models here.


class Patients(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    patient_code = models.CharField(max_length=100, unique=True)
    datetime = models.DateField(auto_now_add=True)


class PatientUploads(models.Model):
    patient = models.ForeignKey(Patients, on_delete=models.CASCADE)
    image = models.FileField(upload_to='uploads/')
    predicted_class = models.CharField(max_length=100, null=True, default=None)
    datetime = models.DateField(auto_now_add=True)


