from django.urls import path

from .views import ImageList, ImageDetail, ImageCreate
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('images/', ImageList.as_view()),
    path('images/<int:pk>/', ImageDetail.as_view()),
    path('images/create/', ImageCreate.as_view()),
]
