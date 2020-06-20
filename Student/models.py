from django.db import models
from django.contrib.auth.models import User

# Create your models here.
gender = [('Male', 'Male'), ('Female', 'Female')]
classes = [('One', 'One'), ('Two', 'Two'), ('Three', 'Three'), ('Four', 'Four'), ('Five', 'Five'), ('Six', 'Six'), ('Seven', 'Seven'),
           ('Eight', 'Eight'), ('Nine', 'Nine'), ('Ten', 'Ten')]
blood_group = [('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'),
               ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-')]

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='student/images')
    classes = models.CharField(max_length=10, choices=classes)
    roll = models.CharField(max_length=20)
    gender = models.CharField(max_length=10, choices=gender)
    dob = models.DateField()
    blood_group = models.CharField(max_length=5, choices=blood_group, blank=True)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=25)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name

    @property
    def get_id(self):
        return self.user.id

    @property
    def get_name(self):
        return self.user.first_name + " " + self.user.last_name
