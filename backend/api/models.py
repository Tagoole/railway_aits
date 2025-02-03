from random import choices
from django.db import models
from django.contrib.auth.models import AbstractUser

'''
Remove the option of head of department
added year of study
'''
class CustomUser(AbstractUser):
    GENDER_CHOICES = [
        ('male','Male'),
        ('female','Female'),
    ]
    ROLE_CHOICES = [
        ('student','Student'),
        ('lecturer','lecturer'),
        ('head_of_department','Head of Department'),
        ('academic_registrar','academic_registrar'),
    ]
    role = models.CharField(max_length=30, choices = ROLE_CHOICES, default = 'student')
    gender = models.CharField(max_length = 20,choices = GENDER_CHOICES, null = True, editable = True)
    year_of_study = models.IntegerField(null = True, editable= True)    
    city = models.CharField(max_length=30, null = True, editable = True)
    
    def __str__(self):
        return self.username

'''
do some research about code
'''
class Department(models.Model):
    department_name = models.CharField(max_length=100, unique = True) 
    code = models.CharField(max_length=20, unique = True)
    description = models.TextField()
    
    def __str__(self):
        return self.department_name
'''
department checkout
'''
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
#    image = models.ImageField(upload_to='media/images/', blank = True,null = True)
    status = models.CharField(max_length=30, choices = STATUS_CHOICES, default = 'pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    lecturer = models.ForeignKey(CustomUser,on_delete=models.SET_NULL,null = True, related_name = "lecturer",limit_choices_to={'role':'lecturer'})
    registrar = models.ForeignKey(CustomUser,on_delete=models.SET_NULL,null = True, related_name = "registrar",limit_choices_to={'role':'academic_registrar'}) 
    
    class Meta:
        ordering = ['updated_at','created_at']
    
    def __str__(self):
        return self.issue_type



class Audit_Trail(models.Model):
    ACTION_CHOICES = [
        ('created','Created'),
        ('assigned','Assigned'),
        ('resolved','Resolved'),
        ('updated','Updated'),
        ('forwarded','Forwarded'),
        ('closed','Closed'),
    ]
    
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE,related_name='audit_trail',)
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    action = models.CharField(max_length=20, choices = ACTION_CHOICES,default = 'created')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)
    comment = models.TextField(blank=True,null = True)
    previous_status = models.CharField(blank = True, null = True,max_length=30)
    new_status = models.CharField(blank = True, null = True,max_length=30)
    
    def __str__(self):
        return f"{self.user.username}-{self.action} on {self.issue} at {self.updated_at}"
    
    class Meta:
        ordering = ['updated_at','created_at']