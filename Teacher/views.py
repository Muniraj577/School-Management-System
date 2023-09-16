from django.shortcuts import render, redirect, get_object_or_404

from . import models, forms
from django.db.models import Sum
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='schooldashboard:login')
def index(request):
    teachers = models.Teacher.objects.all().filter(status=True)
    return render(request, 'Teacher/teacher_index.html', {'teachers': teachers})


def add_teacher(request):
    form1 = forms.TeacherForm()
    form2 = forms.TeacherExtraForm()
    context = {
        'form1': form1,
        'form2': form2
    }
    if request.method == 'POST':
        form1 = forms.TeacherForm(request.POST)
        form2 = forms.TeacherExtraForm(request.POST, request.FILES)
        if form1.is_valid() and form2.is_valid():
            user = form1.save()
            user.set_password(user.password)
            user.save()
            f2 = form2.save(commit=False)
            f2.user = user
            f2.status = True
            user2 = f2.save()
            teacher_group = Group.objects.get_or_create(name='Teacher')
            teacher_group[0].user_set.add(user)
        return redirect('Teacher:teacher_index')
    return render(request, 'Teacher/add_teacher.html', context=context)


# def update_teacher(request, pk):
#     teacher = models.Teacher.objects.get(id=pk)
#     user = models.User.objects.get(id=teacher.user_id)
#     form1 = forms.TeacherForm(instance=user)
#     form2 = forms.TeacherExtraForm(instance=teacher)
#     context = {
#         'teacher': teacher,
#         'user': user,
#         'form1': form1,
#         'form2': form2
#     }
#     if request.method == 'POST':
#         form1 = forms.TeacherForm(request.POST, instance=user)
#         form2 = forms.TeacherExtraForm(request.POST, instance=teacher)
#         if form1.is_valid() and form2.is_valid():
#             user = form1.save(commit=False)
#             # user.set_password(user.password)
#             user.save(update_fields=['first_name', 'last_name', 'email', 'username'])
#             f2 = form2.save(commit=False)
#             f2.status = True
#             f2.save(update_fields=['phone', 'address', 'salary', 'status'])
#             return redirect('Teacher:teacher_index')
#     return render(request, 'Teacher/update_teacher.html', context)

def update_teacher(request, pk):
    teacher = get_object_or_404(models.Teacher, pk=pk)
    user = teacher.user
    if request.method == 'POST':
        form1 = forms.TeacherUpdateForm(request.POST, instance=user)
        form2 = forms.TeacherUpdateExtraForm(request.POST, instance=teacher)
        if form1.is_valid() and form2.is_valid():
            form1.save()
            form2.instance.status = True
            form2.save()
            return redirect('Teacher:teacher_index')
    else:
        form1 = forms.TeacherUpdateForm(instance=user)
        form2 = forms.TeacherUpdateExtraForm(instance=teacher)
    context = {
        'teacher': teacher,
        'user': user,
        'form1': form1,
        'form2': form2
    }
    return render(request, 'Teacher/update_teacher.html', context)


def delete_teacher(request, pk):
    teacher = models.Teacher.objects.get(id=pk)
    user = teacher.user
    user.delete()
    teacher.delete()
    return redirect('Teacher:teacher_index')


def view_teacher_salary(request):
    teachers = models.Teacher.objects.all();
    return render(request, 'Teacher/view_salary.html', {'teachers': teachers})
