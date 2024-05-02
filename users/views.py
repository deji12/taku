from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Student, Employee, DeregistrationRequest
from .forms import StudentCreationForm, EmployeeCreationForm, DeregistrationRequestForm
from django.db import IntegrityError
from chat.models import *
from assignment.models import *
from assessment.models import Assessment
import logging
from django.contrib.auth import get_user_model

def authenticate(email, password):
    UserModel = get_user_model()
    
    try:
        get_user = UserModel.objects.get(email=email)
        print('-----------------------')
        print(get_user)
        if get_user.check_password(password):
            return get_user
        else:
            print('returning none')
            return None

    except User.DoesNotExist:
        return None

def loginPage(request):
    page = "login" 
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(email, password)

        if user is not None:
            login(request, user)
            # if user.position == "Lecturer":
            #     return redirect('users:lecturer_dashboard')  # Redirect to lecturer dashboard
            # elif user.position == "Internship Coordinator":
            #     return redirect('users:coordinator_dashboard')  # Redirect to coordinator dashboard
            # else:
            #     return redirect('users:student_dashboard')  # Redirect to student dashboard
            return redirect('users:student_dashboard')
        else :
            print(None)

    context = {"page":page}
    return render(request, 'users/login_register.html',context)

def logoutPage(request):
    logout(request)
    return redirect('users:login-page')

#Internship coordinator dashboard
def coordinator_dashboard(request):
    lecturers = Employee.objects.all()
    students = Student.objects.all()
    pending_de_registrations = DeregistrationRequest.objects.all()

    # Filter students based on assignment status
    assigned_students = students.filter(assignment__isnull=False)
    unassigned_students = students.filter(assignment__isnull=True)

    # Calculate assessment progress for each student
    for student in students:
        assessments = Assessment.objects.filter(student=student)
        total_marks = 0
        total_possible_marks = 0
        for assessment in assessments:
            if assessment.assessment_one_marks is not None:
                total_marks += assessment.assessment_one_marks
                total_possible_marks += 100
            if assessment.assessment_two_marks is not None:
                total_marks += assessment.assessment_two_marks
                total_possible_marks += 100
        
        if total_possible_marks > 0:
            progress_percentage = (total_marks / total_possible_marks) * 100
            student.assessment_progress = round(progress_percentage, 2)
        else:
            student.assessment_progress = 0

    return render(request, 'users/coordinator_dashboard.html', {
        'lecturers': lecturers,
        'all_students': students,
        'assigned_students': assigned_students,
        'unassigned_students': unassigned_students,
        'pending_de_registrations': pending_de_registrations
    })
    

#Lecturer dashboard
def lecturer_dashboard(request ):
    lecturer = Employee.objects.get(username='mmusara')
    assigned_students = Assignment.objects.filter(lecturer=lecturer)
    students = [assignment.student for assignment in assigned_students]
    return render(request, 'users/lecturer_dashboard.html', {'students': students, "lecturer":lecturer})
	# lecturer = request.User
	# students = Student.objects.filter(lecturer=lecturer)
        
        

#Student view
def student_dashboard(request):
	# messages = Message.objects.filter(Student=request.user){'messages': messages, 'meetings': meetings}
	return render(request, 'users/student_dashboard.html')

#User registration
def registerStudent(request):
    type = "Student"
    if request.method == 'POST':
        form = StudentCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('users:student_dashboard')  # Redirect to success page
    else:
        form = StudentCreationForm()
    return render(request, 'users/login_register.html', {'form': form})

def registerStaff(request):
    if request.method == 'POST':
        form = EmployeeCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            if user.position == "Lecturer":
                return redirect('users:lecturer_dashboard')  # Redirect to lecturer dashboard
            else:
                return redirect('users:coordinator_dashboard')  # Redirect to coordinator dashboard
    else:
        form = EmployeeCreationForm()
    return render(request, 'users/login_register.html', {'form': form})

#lecturer view of a student that they are assessing
def lecturer_student_detail(request, student_username):
    student = Student.objects.get(username=student_username)
    messages = Message.objects.filter(lecturer=request.user, student=student)
    return render(request, 'users/lecturer_student_detail.html', {'student': student, 'messages': messages})

#Student Deregistration
@login_required
def initiate_deregistration(request, student_username):
    student = Student.objects.get(username=student_username)
    
    if request.method == 'POST':
        form = DeregistrationRequestForm(request.POST)
        if form.is_valid():
            reason = form.cleaned_data['reason']
            lecturer = request.user
            
            # Check if the lecturer belongs to the 'Lecturer' group
            if lecturer.groups.filter(name='Lecturer').exists():
                # Create the deregistration request
                DeregistrationRequest.objects.create(
                    student=student,
                    lecturer=lecturer,
                    reason=reason,
                    status='pending'
                )
                # Redirect to the lecturer dashboard after successful request creation
                return redirect('lecturer_dashboard')
            else:
                # Handle the case where lecturer is not a lecturer
                # This could be due to incorrect user-to-employee mapping
                # Redirect or display an error message
                pass
    else:
        form = DeregistrationRequestForm()
        
    return render(request, 'users/initiate_deregistration.html', {'form': form})

def approve_deregistration(request, request_id):
    request = DeregistrationRequest.objects.get(id=request_id)
    request.status = 'approved'
    request.save()
    return redirect('internship_coordinator_dashboard')

def reject_deregistration(request, request_id):
    request = DeregistrationRequest.objects.get(id=request_id)
    request.status = 'rejected'
    request.save()
    return redirect('internship_coordinator_dashboard')




