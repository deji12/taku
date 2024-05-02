from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import LogbookEntry


def student_view(request):
    if request.method == 'POST':
        student = request.user
        date = request.POST['date']
        activity = request.POST['activity']
        LogbookEntry.objects.create(student=student, date=date, activity=activity)
        messages.success(request, 'Logbook entry added successfully.')
    return render(request, 'logbook/student_view.html')

def lecturer_view(request):
    entries = LogbookEntry.objects.all()
    return render(request, 'logbook/lecturer_view.html', {'entries': entries})