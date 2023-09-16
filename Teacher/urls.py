from django.urls import path
from . import views

app_name = 'Teacher'
urlpatterns = [
    path('teacher', views.index, name='teacher_index'),
    path('teacher-salary', views.view_teacher_salary, name='view_salary'),
    path('add-teacher', views.add_teacher, name='add_teacher'),
    path('update-teacher/<int:pk>', views.update_teacher, name='update_teacher'),
    path('delete-teacher/<int:pk>', views.delete_teacher, name='delete_teacher'),
]
