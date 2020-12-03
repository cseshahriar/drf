from django.urls import path, include
from rest_framework import routers
from .views import EmployeeViewSet

# router for viewset
router = routers.DefaultRouter()
router.register('', EmployeeViewSet)

urlpatterns = [
    path('employees/', include(router.urls)),  # it's multiple urls
]
