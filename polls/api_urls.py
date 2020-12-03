from django.urls import path
from .views import PollAPIView, PollDetailAPIView

urlpatterns = [
    path('', PollAPIView.as_view()),
    path('<int:pk>/', PollDetailAPIView.as_view()),
]
