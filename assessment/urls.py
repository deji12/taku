from django.urls import path
from . import views

app_name = 'assessment'

urlpatterns = [
	path('capture-marks/', views.capture_marks, name='capture_marks'),
]
