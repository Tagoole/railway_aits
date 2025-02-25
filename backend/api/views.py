from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .serializers import IssueSerializer,DepartmentSerializer,Course_unitSerializer,RegisterSerializer
from rest_framework.decorators import APIView
from .models import CustomUser,Department,Issue,Course_unit
from rest_framework.parsers import MultiPartParser,FormParser
from rest_framework import status
from rest_framework.permissions import AllowAny,IsAuthenticated

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



class Registration(APIView):
    permission_classes = [AllowAny]
    def post(self,request):
        data = request.data 
        serializer = RegisterSerializer(data=data)
        if serializer.is_valid():
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