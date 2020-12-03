from django.urls import path
from .views import poll, poll_details

urlpatterns = [
    path('', poll),
    path('<int:pk>/', poll_details),
]
