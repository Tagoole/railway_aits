from .models import CustomUser,Issue,Department
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
        


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'first_name', 'last_name', 'username', 'email', 'password', 'gender']
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, data):
        if data['username']:
            if CustomUser.objects.filter(username=data.get('username')).exists():
                raise serializers.ValidationError("Username already exists.")

        if data['email']:
            if CustomUser.objects.filter(email=data.get('email')).exists():
                raise serializers.ValidationError("Email already taken.")
        return data
