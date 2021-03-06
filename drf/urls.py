"""drf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from employee.views import LoginAPIView, LogoutAPIView

from django.conf import settings
from django.conf.urls.static import static

# api doc
from .aysg import urlpatterns as api_doc_urls

urlpatterns = [
    path('admin/', admin.site.urls),

    # employee urls
    path('api/', include('employee.api_urls')),

    # polls urls
    path('api/polls/', include('polls.api_urls')),

    # images
    path('api/images/', include('images.api_urls')),

    # auth urls
    path('api/app/login/', LoginAPIView.as_view()),
    path('api/app/logout', LogoutAPIView.as_view()),
    path('api/auth/', include('rest_framework.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += api_doc_urls
