from .models import CustomUser,Issue,Department,Audit_Trail
from rest_framework import serializers

from api import models

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
        
        


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'
        
        
        
        
        
class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = '__all__'
        
        
class Audit_TrailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audit_Trail
        fields = '__all__'