from django.db import models

# Create your models here.
class MyPatient(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    gender = models.CharField(max_length=6)
    age = models.IntegerField()
    dob = models.DateField()
    datetime = models.DateTimeField()
    medicalhistory = models.TextField()


    def __str__(self):
        return self.name
    

class Doctor(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.CharField(max_length=14)
    aos = models.CharField(max_length=20)


    def __str__(self):
        return self.name
    



class MyAppointment(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    datetime = models.DateTimeField()
    department = models.CharField(max_length=30)
    doctor = models.CharField(max_length=20)
    message = models.TextField()

    def __str__(self):
        return self.name