from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('login/', views.loginPage, name="login-page"),
    path('logout/', views.logoutPage, name="logout-page"),
    path('register-student/', views.registerStudent, name="register-student"),
    path('register-staff/', views.registerStaff, name="register-staff"),
    path('lecturer_dashboard/', views.lecturer_dashboard, name='lecturer_dashboard'),
    path('student_dashboard/', views.student_dashboard, name='student_dashboard'),
    path('coordinator_dashboard/', views.coordinator_dashboard, name='coordinator_dashboard'),
    path('lecturer_student_detail/',views.lecturer_student_detail, name='lecturer_student_detail'),
    
    #De-regsistration
    path('students/<str:student_username>/deregister/', views.initiate_deregistration, name='initiate_deregistration'),
    path('deregistration_requests/<int:request_id>/approve/', views.approve_deregistration, name='approve_deregistration'),
    path('deregistration_requests/<int:request_id>/reject/', views.reject_deregistration, name='reject_deregistration'),
    
]
