from django.shortcuts import render, redirect
from .models import Assessment
from .forms import AssessmentForm, AssessmentFilterForm

def capture_marks(request):
	if request.method == 'POST':
		assessment_form = AssessmentForm(request.POST)
		if assessment_form.is_valid():
			assessment = assessment_form.save(commit=False)
			assessment.save()
			return redirect('capture_marks')
	else:
		assessment_form = AssessmentForm()
	return render(request, 'assessment/capture_marks.html', {'assessment_form': assessment_form})

#Extraction of marks
def extract_assessment_data(request):
    form = AssessmentFilterForm(request.GET)
    assessments = Assessment.objects.all()

    if form.is_valid():
        start_date = form.cleaned_data['start_date']
        end_date = form.cleaned_data['end_date']
        min_assessment_one_marks = form.cleaned_data['min_assessment_one_marks']
        max_assessment_one_marks = form.cleaned_data['max_assessment_one_marks']
        min_assessment_two_marks = form.cleaned_data['min_assessment_two_marks']
        max_assessment_two_marks = form.cleaned_data['max_assessment_two_marks']


        if start_date:
            assessments = assessments.filter(date__gte=start_date)
        if end_date:
            assessments = assessments.filter(date__lte=end_date)
        if min_assessment_one_marks:
            assessments = assessments.filter(assessment_one_marks__gte=min_assessment_one_marks)
        if max_assessment_one_marks:
            assessments = assessments.filter(assessment_one_marks__lte=max_assessment_one_marks)
        if min_assessment_two_marks:
            assessments = assessments.filter(assessment_two_marks__gte=min_assessment_two_marks)
        if max_assessment_two_marks:
            assessments = assessments.filter(assessment_two_marks__lte=max_assessment_two_marks)

    context = {'form': form, 'assessments': assessments}
    return render(request, 'assessment/assessment_extract.html', context)