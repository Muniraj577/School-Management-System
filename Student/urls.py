from django.urls import path
from . import views

app_name = 'student'
urlpatterns = [
    path('student', views.index, name='student_index'),
    path('add-student', views.add_student, name='add_student'),
    path('update-student/<int:pk>', views.update_student, name='update_student'),
    path('delete-student/<int:pk>', views.delete_student, name='delete_student'),
]
