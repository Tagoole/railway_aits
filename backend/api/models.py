from django.db import models
from django.contrib.auth.models import AbstractUser
import shortuuid
from random import randint
from django.utils import timezone
from django.conf import settings
from django.core.mail import send_mail
# add other option in issue dropdown
class CustomUser(AbstractUser):
    GENDER_CHOICES = [
        ('male','Male'),
        ('female','Female'),
    ]
    ROLE_CHOICES = [
        ('student','Student'),
        ('lecturer','lecturer'),
        ('academic_registrar','academic_registrar'),
    ]
    
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100,unique=True,null=False,blank = False)
    email = models.EmailField(unique=True)
    is_email_verified = models.BooleanField(default=False)
    confirm_password = models.CharField(max_length=50)
    role = models.CharField(max_length=30, choices = ROLE_CHOICES)
    image = models.ImageField(upload_to='profile_pictures/', null = True, blank = True)
    gender = models.CharField(max_length = 20,choices = GENDER_CHOICES,editable = True)
    program = models.ForeignKey('Program',on_delete= models.CASCADE, related_name='programs',null = True, blank=True)    
    city = models.CharField(max_length=30, editable = True)
    token = models.CharField(max_length=50,null= True)
    
    def __str__(self):
        return self.username

class Department(models.Model):
    department_name = models.CharField(max_length=100, unique = True) 
    description = models.TextField()
    
    def __str__(self):
        return self.department_name
    
class Course_unit(models.Model):
    course_unit_code = models.CharField(max_length=10)
    course_unit_name = models.CharField(max_length=200)

    def __str__(self):
        return self.course_unit_name
    
class Program(models.Model):
    program_name = models.CharField(max_length=100)
    course_units = models.ManyToManyField(Course_unit,related_name='course_units', blank=True)
    
    def __str__(self):
        return self.program_name
    
# User doesnot need to select program because it is already in the system
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
    SEMESTER_CHOICES = [
        ('one','One'),
        ('two','Two')
    ]
    
    STUDY_YEARS = [
        ('1st_year','1st Year'),
        ('2nd_year','2nd Year'),
        ('3rd_year','3rd Year'),
        ('4th_year','4th Year'),
        ('5th_year','5th Year')
    ]
    
    student = models.ForeignKey(CustomUser,on_delete=models.SET_NULL,null = True, related_name='issues', limit_choices_to={'role':'student'})
    issue_type = models.CharField(max_length=30, choices = ISSUE_CHOICES)
    course_unit = models.ForeignKey(Course_unit,on_delete= models.CASCADE)
    description = models.TextField()
    image = models.ImageField(upload_to='issues/',null = True,blank= True)
    status = models.CharField(max_length=30, choices = STATUS_CHOICES, default = 'pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    lecturer = models.ForeignKey(CustomUser,on_delete=models.SET_NULL,null = True, related_name = "lecturer_issues",limit_choices_to={'role':'lecturer'})
    registrar = models.ForeignKey(CustomUser,on_delete=models.SET_NULL,null = True, related_name = "registrar_issues",limit_choices_to={'role':'academic_registrar'}) 
    year_of_study = models.CharField(max_length=20,choices = STUDY_YEARS)
    semester = models.CharField(max_length = 10,choices = SEMESTER_CHOICES)

    class Meta:
        ordering = ['updated_at','created_at']
    
    def __str__(self):
        return self.issue_type
    
class Registration_Token(models.Model):
    ROLE_CHOICES = [
        ('lecturer','lecturer'),
        ('academic_registrar','academic_registrar'),
    ]
    role = models.CharField(max_length=20, choices = ROLE_CHOICES)
    email = models.EmailField(unique=True)
    token = models.CharField(default=shortuuid.uuid,max_length=50)
    
    
    
    def __str__(self):
        return f'Token for {self.email}'
    

class Verification_code(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    code = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_verified = models.BooleanField(default=False)
    
    def is_verification_code_expired(self):
        expiration_time = self.created_at + timezone.timedelta(minutes=10)
        return timezone.now() > expiration_time
    
    @classmethod
    def resend_verification_code(cls,user):
        try:
            cls.objects.filter(user = user).delete()
    
            new_verification_code = randint(10000,99999)
            verification = cls.objects.create(user = user,code= new_verification_code)
        except Exception as e:
            return {'Error':e}

        try:
            subject = 'Email verification Code Resend..'
            message = f"Hello, your Verification code that has been resent is: {new_verification_code}"
            receipient_email= user.email
            send_mail(subject,message,settings.EMAIL_HOST_USER,[receipient_email],fail_silently=False)
        except Exception as e:
            return {'Error':e}
        
        return {'Message':'Email verification code resent successfully...'}
        
    def __str__(self):
        return f'Verification for {self.user.username} --- {self.code}'