from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import IssueSerializer,DepartmentSerializer,UserSerializer,Audit_TrailSerializer
from .models import CustomUser,Department,Issue,Audit_Trail
from rest_framework.parsers import MultiPartParser,FormParser

class IssueViewSet(ModelViewSet):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    parser_classes = (MultiPartParser,FormParser)
    
    def create(self, request, *args, **kwargs):
        student = request.data['student']
        issue_type = request.data['issue_type']
        course_unit_code = request.data['course_unit_code']
        course_unit_name = request.data['course_unit_name']
        description = request.data['description']
        image = request.data['image']
        status = request.data['status']
        created_at = request.data['created_at']
        updated_at = request.data['updated_at']
        registrar = request.data['registrar']
        
        Issue.objects.create(
            student = student,
            issue_type = issue_type,
            course_unit_code = course_unit_code,
            course_unit_name = course_unit_name,
            description = description,
            image = image,
            status = status,
            created_at = created_at,
            updated_at = updated_at,
            registrar = registrar
        )
        return Response("Issue created Successfully")
    
    
class DepartmentViewSet(ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    
class Audit_TrailViewSet(ModelViewSet):
    queryset = Audit_Trail.objects.all()
    serializer_class = Audit_TrailSerializer