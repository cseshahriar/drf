from django.urls import path
from .views import (
    # APIViews
    PollAPIView,
    PollDetailAPIView,

    # generics
    PollListView
)

urlpatterns = [
    path('', PollAPIView.as_view()),
    path('<int:pk>/', PollDetailAPIView.as_view()),

    # generics
    path('generic/', PollListView.as_view()),
    path('generic/<int:pk>/', PollListView.as_view()),
]
