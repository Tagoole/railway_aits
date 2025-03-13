from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .serializers import *
from rest_framework.decorators import APIView, api_view
from .models import *
from rest_framework.parsers import MultiPartParser,FormParser
from rest_framework import status
from rest_framework.permissions import AllowAny,IsAuthenticated
from django.contrib.auth.models import Group

class IssueViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    parser_classes = (MultiPartParser,FormParser)
    
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"request": self.request})
        return context
    
    
    
class DepartmentViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class Course_unitViewSet(ModelViewSet):
    queryset = Course_unit.objects.all()
    serializer_class = Course_unitSerializer

class ProgramViewSet(ModelViewSet):
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer
    
    
'''
registration token
'''
class Registration(APIView):
    permission_classes = [AllowAny]
    def post(self,request):
        data = request.data 
        serializer = RegisterSerializer(data=data)
        if serializer.is_valid():
            print(data)
            validated_data = serializer.validated_data
            password = validated_data.pop('password')
            
            user = CustomUser(**validated_data)
            user.set_password(password)
            user.save()
            return Response({
                "message":"User Created Successfully",
                "data":validated_data
            }, status= status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def assign_user_group(self, user):
        """Assign user to a group based on their role."""
        role_to_group = {
            "student": "Students",
            "lecturer": "Lecturers",
            "academic_registrar": "Registrars"
        }
        
        group_name = role_to_group.get(user.role)  # Get the group name based on role
        if group_name:
            group, created = Group.objects.get_or_create(name=group_name)  # Ensure group exists
            user.groups.add(group)


    