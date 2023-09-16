from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users

# Create your views here.

@login_required(login_url='schooldashboard:login')
@allowed_users(allowed_roles=['Admin', 'Teacher', 'Student'])
def admin_dashboard(request):
    return render(request, 'schooldashboard/dashboard.html')

@unauthenticated_user
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('schooldashboard:admin-dashboard')
        else:
            messages.error(request, 'Username or Password incorrect!')
    return render(request, 'schooldashboard/login.html')


def logout(request):
    auth.logout(request)
    return redirect('schooldashboard:login')

