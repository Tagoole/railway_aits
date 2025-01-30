from rest_framework.decorators import api_view
from rest_framework.response import Response
#from .serializers import IssueSerializer,DepartmentSerializer,UserSerializer
#from .models import CustomUser,Department,Issue

@api_view(['GET','POST'])
def index(request):
    if request.method == 'GET':
        return Response({"message": "Welcome to the Academic Issue Tracking System API"})