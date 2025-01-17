from django.db import models

class UserProfile(models.Model):
    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    password = models.CharField(max_length=128)
    dob = models.DateField()
    phone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    state = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    panchayat = models.CharField(max_length=100)

    def __str__(self):
        return self.username
