from django.urls import path, include
from .views import IssueViewSet,DepartmentViewSet,Audit_TrailViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'issues', IssueViewSet,'issues')
router.register(r'department',DepartmentViewSet,'department')
router.register(r'audit_trail',Audit_TrailViewSet,'audit_trail')

urlpatterns = [
    path('',include(router.urls))
   
]
