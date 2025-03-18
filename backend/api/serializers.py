from .models import *
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
            
class IssueSerializer(serializers.ModelSerializer):
    student = serializers.StringRelatedField()
    registrar = serializers.StringRelatedField()
    course_unit = Course_unitSerializer()
    class Meta:
        model = Issue
        fields = ['id','student','issue_type','course_unit','description','image','status','created_at','updated_at','registrar','year_of_study','semester']

class Student_RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        #fields = "__all__"
        fields = ['id', 'first_name', 'last_name', 'username', 'email', 'password','confirm_password', 'gender','program']
        
        
        extra_kwargs = {
            'password': {'write_only': True},
            'confirm_password': {'write_only': True},
            }

    def validate(self, data):
        password = data.get('password')
        confirm_password = data.get('confirm_password')
        if CustomUser.objects.filter(username=data.get('username')).exists():
            raise serializers.ValidationError("Username already exists.")

    
        if CustomUser.objects.filter(email=data.get('email')).exists():
            raise serializers.ValidationError("Email already taken.")
        
        if password != confirm_password:
            raise serializers.ValidationError("Passwords don't match....")
        
        return data
    
    def create(self, validated_data):
        """Create a new user with hashed password."""
        password = validated_data.pop('password')  # Extract password
        user = CustomUser(**validated_data)  # Create user instance without saving
        user.set_password(password)  # Hash the password
        user.save()  # Save user with hashed password
        return user

class Lecturer_and_Registrar_RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        #fields = "__all__"
        fields = ['id', 'first_name', 'last_name', 'username', 'email', 'password','confirm_password', 'gender','token']
        
        
        extra_kwargs = {
            'password': {'write_only': True},
            'confirm_password': {'write_only': True},
            }

    def validate(self, data):
        password = data.get('password')
        confirm_password = data.get('confirm_password')
        if CustomUser.objects.filter(username=data.get('username')).exists():
            raise serializers.ValidationError("Username already exists.")

    
        if CustomUser.objects.filter(email=data.get('email')).exists():
            raise serializers.ValidationError("Email already taken.")
        
        if password != confirm_password:
            raise serializers.ValidationError("Passwords don't match....")
        
        return data
    
    def create(self, validated_data):
        """Create a new user with hashed password."""
        password = validated_data.pop('password')  # Extract password
        user = CustomUser(**validated_data)  # Create user instance without saving
        user.set_password(password)  # Hash the password
        user.save()  # Save user with hashed password
        return user
    
    
class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = '__all__'


class Registration_Token_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Registration_Token
        fields = '__all__'