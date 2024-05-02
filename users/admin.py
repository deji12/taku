from django.contrib import admin
from .models import Student, Employee, DeregistrationRequest


admin.site.register(Employee)
admin.site.register(Student)
admin.site.register(DeregistrationRequest)