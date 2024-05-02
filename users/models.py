from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission, PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager

POSITION_CHOICES = [
    ('Lecturer', 'Lecturer'),
    ('Internship Coordinator', 'Internship Coordinator')
]
STATUS_CHOICES = [('pending','pending'), ('approved','approved'), ('rejected','rejected')]

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

class User(AbstractUser, PermissionsMixin):
    username = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    
    is_active = models.BooleanField(default=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','first_name', 'last_name','phone_number']
    
    objects = UserManager()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class StudentManager(UserManager):
    pass

class Student(User):
    reg_number = models.CharField(max_length=50, unique=True)
    company = models.CharField(max_length=50)
    programme = models.CharField(max_length=50)
    date_started = models.DateField()
    job_title = models.CharField(max_length=100)
    status = models.CharField(max_length=50, default='active')

    objects = StudentManager()

class EmployeeManager(UserManager):
    pass

class Employee(User):
    position = models.CharField(max_length=100, choices=POSITION_CHOICES)

    objects = EmployeeManager()

class DeregistrationRequest(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    lecturer = models.ForeignKey(Employee, on_delete=models.CASCADE)
    reason = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Deregistration Request for {self.student.first_name} {self.student.last_name}"
