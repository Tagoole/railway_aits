from django.urls import path, include
from .views import IssueViewSet,DepartmentViewSet
from rest_framework.routers import DefaultRouter
#from .views import RegisterAPI
router = DefaultRouter()
router.register(r'issues', IssueViewSet,'issues')
router.register(r'department',DepartmentViewSet,'department')


urlpatterns = [
    path('',include(router.urls))
   
]
