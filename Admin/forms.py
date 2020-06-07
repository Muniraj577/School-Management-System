from django import forms
from django.contrib.auth.models import User
from . import models


class AdminUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']


class AdminUserExtraForm(forms.ModelForm):
    class Meta:
        model = models.AdminUser
        fields = ['phone', 'dob', 'gender', 'address', 'status', 'image']


class AdminUserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']


class AdminUserUpdateExtraForm(forms.ModelForm):
    class Meta:
        model = models.AdminUser
        fields = ['phone', 'address', 'status']
