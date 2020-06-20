from django.shortcuts import render, redirect, get_object_or_404

from . import models, forms
from django.db.models import Sum
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from schooldashboard.decorators import unauthenticated_user, allowed_users


# Create your views here.
@allowed_users(allowed_roles=["Admin"])
@login_required(login_url='schooldashboard:login')
def index(request):
    adminUsers = models.AdminUser.objects.all()
    return render(request, 'Admin/admin_index.html', {'adminUsers': adminUsers})


def add_admin_user(request):
    form1 = forms.AdminUserForm()
    form2 = forms.AdminUserExtraForm()
    context = {
        'form1': form1,
        'form2': form2
    }
    if request.method == 'POST':
        form1 = forms.AdminUserForm(request.POST)
        form2 = forms.AdminUserExtraForm(request.POST, request.FILES)
        if form1.is_valid() and form2.is_valid():
            user = form1.save()
            user.set_password(user.password)
            user.save()
            f2 = form2.save(commit=False)
            f2.user = user
            f2.status = True
            user2 = f2.save()
            admin_user_group = Group.objects.get_or_create(name='Admin')
            admin_user_group[0].user_set.add(user)
        return redirect('Admin:admin_index')
    return render(request, 'Admin/add_admin_user.html', context=context)


def update_admin_user(request, pk):
    admin_user = get_object_or_404(models.AdminUser, pk=pk)
    user = admin_user.user
    if request.method == 'POST':
        form1 = forms.AdminUserUpdateForm(request.POST, instance=user)
        form2 = forms.AdminUserUpdateExtraForm(request.POST, instance=admin_user)
        if form1.is_valid() and form2.is_valid():
            form1.save()
            form2.instance.status = True
            form2.save()
            return redirect('Admin:admin_index')
    else:
        form1 = forms.AdminUserUpdateForm(instance=user)
        form2 = forms.AdminUserUpdateExtraForm(instance=admin_user)
    context = {
        'admin_user': admin_user,
        'user': user,
        'form1': form1,
        'form2': form2
    }
    return render(request, 'Admin/update_admin_user.html', context)


def delete_admin_user(request, pk):
    admin_user = models.AdminUser.objects.get(id=pk)
    user = admin_user.user
    user.delete()
    admin_user.delete()
    return redirect('Admin:admin_index')
