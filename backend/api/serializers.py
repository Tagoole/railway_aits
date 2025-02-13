from .models import CustomUser,Issue,Department,Audit_Trail
from rest_framework import serializers

from api import models

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id','first_name','last_name','email','password','role','gender','year_of_study']
        
        

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'
        
        
class IssueSerializer(serializers.ModelSerializer):
    student = UserSerializer()
    #lecturer = UserSerializer()
    registrar = UserSerializer()
    #department = DepartmentSerializer()
    class Meta:
        model = Issue
        fields = ['id','student','issue_type','course_unit_code','course_unit_name','description','image','status','created_at','updated_at','registrar']
        
