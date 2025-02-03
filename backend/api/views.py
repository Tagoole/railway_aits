from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import IssueSerializer,DepartmentSerializer,UserSerializer,Audit_TrailSerializer
from .models import CustomUser,Department,Issue,Audit_Trail


class IssueViewSet(ModelViewSet):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    
    
class DepartmentViewSet(ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    
class Audit_TrailViewSet(ModelViewSet):
    queryset = Audit_Trail.objects.all()
    serializer_class = Audit_TrailSerializer