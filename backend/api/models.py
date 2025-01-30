from random import choices
from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('student','Student'),
        ('lecturer','lecturer'),
        ('head_of_department','Head of Department'),
        ('academic_registrar','academic_registrar'),
    ]
    role = models.CharField(max_length=30, choices = ROLE_CHOICES, default = 'student')
    
    def __str__(self):
        return self.username


class Department(models.Model):
    department_name = models.CharField(max_length=100, unique = True) 
    code = models.CharField(max_length=20, unique = True)
    description = models.TextField()
    
    def __str__(self):
        return self.department_name

class Issue(models.Model):
    ISSUE_CHOICES = [
        ('missing_marks','Missing Marks'),
        ('appeal','Appeal'),
        ('correction','Correction'),
    ]
    
    STATUS_CHOICES = [
        ('pending','Pending'),
        ('resolved','Resolved'),
        ('in_progress','In Progress'),
    ]
    
    student = models.ForeignKey(CustomUser,on_delete=models.SET_NULL,null = True, related_name='issues', limit_choices_to={'role':'student'})
    department = models.ForeignKey(Department, on_delete=models.CASCADE,null = True)
    issue_type = models.CharField(max_length=30, choices = ISSUE_CHOICES)
    course_code = models.CharField(max_length=30)
    course_name = models.CharField(max_length=150)
    description = models.TextField()
    status = models.CharField(max_length=30, choices = STATUS_CHOICES, default = 'pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    lecturer = models.ForeignKey(CustomUser,on_delete=models.SET_NULL,null = True, related_name = "lecturer",limit_choices_to={'role':'lecturer'})
    registrar = models.ForeignKey(CustomUser,on_delete=models.SET_NULL,null = True, related_name = "registrar",limit_choices_to={'role':'academic_registrar'})
    
    def __str__(self):
        return self.issue_type


