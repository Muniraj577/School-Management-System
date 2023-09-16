from django.urls import path
from . import views

app_name = 'schooldashboard'

urlpatterns = [
    path('admin-dashboard', views.admin_dashboard, name='admin-dashboard'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
]