from django import forms
from .models import Assignment
from users.models import Student

class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ('lecturer',)

class DeRegistrationForm(forms.ModelForm):
	class Meta:
		model = Student
		fields = ('status',)