from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .serializers import *
from rest_framework.decorators import APIView, api_view
from .models import *
from rest_framework.parsers import MultiPartParser,FormParser
from rest_framework import status
from rest_framework.permissions import AllowAny,IsAuthenticated
from django.contrib.auth.models import Group
from django.core.mail import send_mail,EmailMessage,EmailMultiAlternatives
from django.conf import settings

class IssueViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    
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
    
class Lecturer_and_Registrar_Registration(APIView):
    permission_classes = [AllowAny]
    def post(self,request):
        data = request.data.copy()
        token_value = data['token']
        email_value = data['email']
        
        token_object = Registration_Token.objects.filter(token=token_value, email=email_value).first()
        if token_object:
            data['role'] = token_object.role 
            data['is_email_verified'] = True
            print("Updated data:", data)
            
            
        serializer = Lecturer_and_Registrar_RegisterSerializer(data=data)
        if serializer.is_valid():
            user = serializer.save()  # Save user using serializer
            return Response({
                "message": "User Created Successfully",
                "user": {
                    "id": user.id,
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "username": user.username,
                    "email": user.email,
                    "gender": user.gender,
                    "role":user.role,
                    "program": user.program.id if user.program else None,
                    "is_email_verified": user.is_email_verified,
                }
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    
class Student_Registration(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = Student_RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()  # Save user using serializer
            return Response({
                "message": "User Created Successfully",
                "user": {
                    "id": user.id,
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "username": user.username,
                    "email": user.email,
                    "role":user.role,
                    "gender": user.gender,
                    "program": user.program.id if user.program else None,
                    "is_email_verified": user.is_email_verified,
                }
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class Registration_Token_viewset(ModelViewSet):
    queryset = Registration_Token.objects.all()
    serializer_class = Registration_Token_Serializer
    http_method_names = ['get','post','delete']
    
    def create(self,request):
        serializer = self.get_serializer(data = request.data)
        
        if serializer.is_valid():
            token_instance = serializer.save()
            
            subject = "Your Registration Token for the Academic Issue Tracking System"
            message = f"Hello, your registration token is: {token_instance.token}"
            recipient_email = token_instance.email
            
            try:
                send_mail(subject,message,settings.EMAIL_HOST_USER,[recipient_email],fail_silently=False,)
                return Response({"message": "Token created and email sent!"}, status=status.HTTP_201_CREATED)
            
            
            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

    