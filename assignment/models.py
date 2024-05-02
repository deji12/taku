from django.db import models
from users.models import Student, Employee
from django.utils import timezone
from users.models import User

class Assignment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    lecturer = models.ForeignKey(Employee, on_delete=models.CASCADE)
    assessment_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"{self.student} {self.lecturer} {self.assessment_date}"
    
    def get_messages(self):

        return AssignmentMessages.objects.filter(assignment=self)
    

class AssignmentMessages(models.Model):

    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()

    
