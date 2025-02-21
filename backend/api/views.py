from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .serializers import IssueSerializer,DepartmentSerializer,Course_unitSerializer
from .models import CustomUser,Department,Issue,Course_unit
from rest_framework.parsers import MultiPartParser,FormParser

class IssueViewSet(ModelViewSet):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    parser_classes = (MultiPartParser,FormParser)
    
    
    
class DepartmentViewSet(ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class Course_unitViewSet(ModelViewSet):
    queryset = Course_unit.objects.all()
    serializer_class = Course_unitSerializer