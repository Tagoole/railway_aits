from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import IssueSerializer,DepartmentSerializer,UserSerializer
from .models import User,Department,Issue


