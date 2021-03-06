"""ProfSkill URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from django.conf.urls import url,include
from django.conf.urls.static import static
from django.conf import settings
from skill import views
from django.contrib.contenttypes.models import ContentType


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name ="index"),
    #url(r'^$', include('skill.urls')),
    path('contact/', views.contact, name="contact"),
    path('inside/', views.inside_view, name="inside"),
    path('service/', views.service, name="service"),
    path('blog/', views.blog_view, name="blog"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

