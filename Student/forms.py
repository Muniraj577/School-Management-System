from django import forms
from django.contrib.auth.models import User
from . import models


class StudentForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']

    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    def clean(self):
        super(StudentForm, self).clean()
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        if first_name == "":
            self._errors['first_name'] = self.error_class(['First name is required.'])

        if last_name == "":
            self._errors['last_name'] = self.error_class(['Last name is required.'])

        if username == "":
            self._errors['username'] = self.error_class(['Username is required.'])

        if email == "":
            self._errors['email'] = self.error_class(['Email is required.'])

        if password == "":
            self._errors['password'] = self.error_class(['Password is required.'])
        return self.cleaned_data




class StudentExtraForm(forms.ModelForm):
    class Meta:
        model = models.Student
        fields = ['classes', 'roll', 'blood_group', 'phone', 'dob', 'gender', 'address', 'status', 'image']

    def __init__(self, *args, **kwargs):
        super(StudentExtraForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class StudentUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']
    def __init__(self, *args, **kwargs):
        super(StudentUpdateForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

class StudentUpdateExtraForm(forms.ModelForm):
    class Meta:
        model = models.Student
        fields = ['classes', 'roll', 'blood_group', 'phone', 'dob', 'gender', 'address', 'status']

    def __init__(self, *args, **kwargs):
        super(StudentUpdateExtraForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
