from django.shortcuts import render, redirect, get_object_or_404

from . import models, forms
from django.db.models import Sum
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from schooldashboard.decorators import unauthenticated_user, allowed_users


# Create your views here.
@login_required(login_url='schooldashboard:login')
def index(request):
    students = models.Student.objects.all()
    return render(request, 'Student/student_index.html', {'students': students})


def add_student(request):
    # form1 = forms.StudentForm()
    # form2 = forms.StudentExtraForm()
    # context = {
    #     'form1': form1,
    #     'form2': form2
    # }
    if request.method == 'POST':
        form1 = forms.StudentForm(request.POST)
        form2 = forms.StudentExtraForm(request.POST, request.FILES)
        if form1.is_valid() and form2.is_valid():
            user = form1.save()
            user.set_password(user.password)
            user.save()
            f2 = form2.save(commit=False)
            f2.user = user
            f2.status = True
            user2 = f2.save()
            student_user_group = Group.objects.get_or_create(name='Student')
            student_user_group[0].user_set.add(user)
            return redirect('student:student_index')
        else:
            return render(request, 'Student/add_student.html', {'form1': form1, 'form2': form2})
    else:
        form1 = forms.StudentForm()
        form2 = forms.StudentExtraForm()
        return render(request, 'Student/add_student.html', {'form1': form1, 'form2': form2})


def update_student(request, pk):
    student = get_object_or_404(models.Student, pk=pk)
    user = student.user
    if request.method == 'POST':
        form1 = forms.StudentUpdateForm(request.POST, instance=user)
        form2 = forms.StudentUpdateExtraForm(request.POST, instance=student)
        if form1.is_valid() and form2.is_valid():
            form1.save()
            form2.instance.status = True
            form2.save()
            return redirect('student:student_index')
    else:
        form1 = forms.StudentUpdateForm(instance=user)
        form2 = forms.StudentUpdateExtraForm(instance=student)
    context = {
        'student': student,
        'user': user,
        'form1': form1,
        'form2': form2
    }
    return render(request, 'Student/update_student.html', context)


def delete_student(request, pk):
    student = models.Student.objects.get(id=pk)
    user = student.user
    user.delete()
    student.delete()
    return redirect('student:student_index')
