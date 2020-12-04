from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter

from .views import (
    # APIViews
    PollAPIView,
    PollDetailAPIView,

    # generics
    PollListView,

    # viewsets
    PollViewSet,
)

# viewsets urls
router = DefaultRouter()
router.register('poll', PollViewSet)

urlpatterns = [

    path('poll/', include(router.urls)),

    path('', PollAPIView.as_view()),
    path('<int:pk>/', PollDetailAPIView.as_view()),

    # generics
    path('generic/', PollListView.as_view()),
    path('generic/<int:pk>/', PollListView.as_view()),

]
