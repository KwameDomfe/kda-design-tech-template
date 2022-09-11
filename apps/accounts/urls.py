
"""aeslWebAppdir URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from apps.website import views
from . import views
from django.conf import settings

app_name = 'accounts'

urlpatterns = [
    path(
        'admin-login/', 
        views.admin_Login, 
        name='admin-login'
    ), 
    path('admin-home/', 
        views.admin_Home, 
        name='admin-home'
    ),
   
    path('admin-login-process/', 
        views.admin_Login_Process, 
        name='admin-login-process'
    ),
    path('staff-login/', 
        views.staff_Login, 
        name='staff-login'), 

   
]