from django.urls import path
from . import views

app_name = 'logbook'

urlpatterns = [
    path('log-task/', views.student_view, name='logbook_student_view'),
    path('review-logbook/', views.lecturer_view, name='logbook_lecturer_view'),
]