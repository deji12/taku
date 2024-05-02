from django.db import models
from users.models import Student

class Assessment(models.Model):
	student = models.ForeignKey(Student, on_delete=models.CASCADE)
	assessment_one_marks = models.IntegerField(null=True, blank=True)
	assessment_two_marks = models.IntegerField(null=True, blank=True)
	date = models.DateTimeField(auto_now_add=True)
