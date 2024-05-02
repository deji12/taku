from django.urls import path
from . import views

app_name = 'assignment'

urlpatterns = [
    path('assign/<str:student_username>', views.assign_student, name='assign_student'),
    path('assignments/', views.assignment_list, name='assignment_list'),
    path('assigned_students/', views.view_assigned_students, name='view_assigned_students'),
    path('initiate_de_registration/<int:student_id>/', views.initiate_de_registration, name='initiate_de_registration'),
	path('approve_de_registration/<int:student_id>/', views.approve_de_registration, name='approve_de_registration'),
]