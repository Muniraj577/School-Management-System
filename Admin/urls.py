from django.urls import path
from . import views

app_name = 'Admin'
urlpatterns = [
    path('admin-user', views.index, name='admin_index'),
    path('add-admin-user', views.add_admin_user, name='add_admin_user'),
    path('update-admin-user/<int:pk>', views.update_admin_user, name='update_admin_user'),
    path('delete-admin-user/<int:pk>', views.delete_admin_user, name='delete_admin_user'),
]