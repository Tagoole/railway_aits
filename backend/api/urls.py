from django.urls import path, include
from .views import IssueViewSet,DepartmentViewSet,Course_unitViewSet
from rest_framework.routers import DefaultRouter
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


#from .views import RegisterAPI
router = DefaultRouter()
router.register(r'issues', IssueViewSet,'issues')
router.register(r'department',DepartmentViewSet,'department')
router.register(r'course_unit',Course_unitViewSet,'course_unit')


urlpatterns = [
    path('',include(router.urls)),
    path("access_token/",TokenObtainPairView.as_view(),name = "access_token"),
    path("refresh_token/",TokenRefreshView.as_view(),name = "refresh_token")
   
]
