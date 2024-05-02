from django.shortcuts import render, redirect
from .models import  Assignment
from .forms import AssignmentForm
from users.models import Employee, Student
from .forms import DeRegistrationForm

def assign_student(request, student_username):
    student = Student.objects.get(username=student_username)
    if request.method == 'POST':
        form = AssignmentForm(request.POST)
        if form.is_valid():
            assignment = form.save(commit=False)
            assignment.student = student
            assignment.save()
            return redirect('assignment:assignment_list')
    else:
        form = AssignmentForm()
    return render(request, 'assignment/assign_student.html', {'form': form, 'student':student})

def assignment_list(request):
    assignments = Assignment.objects.filter(student=request.user)
    return render(request, 'assignment/assignment_list.html', {'assignments': assignments})

#lecturer's view of the students that have been assigned to him
def view_assigned_students(request):
    lecturer = request.user
    assignments = Assignment.objects.filter(lecturer=lecturer)
    students = [assignment.student for assignment in assignments]
    return render(request, 'assignment/view_assigned_students.html', {'students': students})


# De-registration of students from the system
def initiate_de_registration(request, student_first_name):
	student = Student.objects.get(first_name=student_first_name)
	if request.user.employee.position == 'Lecturer' and request.user.employee in student.lecturers.all():
		student.status = 'pending_de_registration'
		student.save()
		return redirect('de_registration_pending')
	return render(request, 'assignments/error.html', {'message': 'Unauthorized'})

def approve_de_registration(request, student_first_name):
	student = Student.objects.get(first_name=student_first_names)
	if request.user.employee.position == 'Internship Coordinator' and student.status == 'pending_de_registration':
		student.delete()
		return redirect('de_registration_success')
	return render(request, 'assignments/error.html', {'message': 'Unauthorized'})