from django import forms
from .models import *

class StudentCreationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = Student
        fields = ['email', 'password', 'username', 'first_name', 'last_name', 'phone_number', 'reg_number', 'company', 'programme', 'date_started', 'job_title']
    

class EmployeeCreationForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['email', 'password', 'username', 'first_name', 'last_name', 'phone_number', 'position']


class DeregistrationRequestForm(forms.ModelForm):
    class Meta:
        model = DeregistrationRequest
        fields = ('reason',)