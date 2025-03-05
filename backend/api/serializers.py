from .models import CustomUser,Issue,Department,Course_unit
from rest_framework import serializers
from api import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id','first_name','last_name','username','email','password','role','gender','year_of_study']
        
        
class Course_unitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course_unit
        fields = "__all__"

        
class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'
        
class LimitedUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username']
            
class IssueSerializer(serializers.ModelSerializer):
    student = LimitedUserSerializer()
    registrar = LimitedUserSerializer()
    class Meta:
        model = Issue
        fields = ['id','student','issue_type','course_unit','description','image','status','created_at','updated_at','registrar']
    '''    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        request = self.context.get('request')
        if request and hasattr(request, 'user'):
            if request.user.role == 'student':
                self.fields.pop('lecturer', None)
        
'''

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
'''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        request = self.context.get('request')
        if request and hasattr(request, 'user'):
            if request.user.role != 'student':
                self.fields.pop('year_of_study', None)
   ''' 