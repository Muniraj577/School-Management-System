from django.db import models
from django.contrib.auth.models import User

# Create your models here.
gender = [('Male', 'Male'), ('Female', 'Female')]


class AdminUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='adminUser/images')
    gender = models.CharField(max_length=10, choices=gender)
    dob = models.DateField()
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=25)
    joindate = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name

    @property
    def get_id(self):
        return self.user.id

    @property
    def get_name(self):
        return self.user.first_name + " " + self.user.last_name
