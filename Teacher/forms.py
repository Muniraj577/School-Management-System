from django import forms
from django.contrib.auth.models import User
from . import models


class TeacherForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']


class TeacherExtraForm(forms.ModelForm):
    class Meta:
        model = models.Teacher
        fields = ['phone', 'dob', 'gender', 'address', 'salary', 'status', 'image']


class TeacherUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']


class TeacherUpdateExtraForm(forms.ModelForm):
    class Meta:
        model = models.Teacher
        fields = ['phone', 'address', 'salary', 'status']
