from django import forms
from .models import Assessment

class AssessmentForm(forms.ModelForm):
	class Meta:
		model = Assessment
		fields = ('assessment_one_marks',)
  
class AssessmentFilterForm(forms.Form):
    start_date = forms.DateField(required=False)
    end_date = forms.DateField(required=False)
    min_assessment_one_marks = forms.IntegerField(required=False)
    max_assessment_one_marks = forms.IntegerField(required=False)
    min_assessment_two_marks = forms.IntegerField(required=False)
    max_assessment_two_marks = forms.IntegerField(required=False)
