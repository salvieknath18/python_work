from django.db import models
from django.contrib.auth.models import User


class Tutor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    address = models.TextField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    timings = models.CharField(max_length=50)
    subjects = models.CharField(max_length=50)
    classes_taught = models.CharField(max_length=50)
    experience = models.CharField(max_length=50)
    qualification = models.CharField(max_length=50)
    class_frequency = models.CharField(max_length=50)
    about = models.TextField(max_length=200)
    objects = models.Manager()

    def __str__(self):
        return self.name
