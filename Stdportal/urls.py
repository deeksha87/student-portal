"""Stdportal URL Configuration

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
from register import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name = 'index'),
    path('register', views.register, name = 'register'),
    path('login', views.user_login, name = 'login'),
    path('view', views.autoClazz, name = 'autoClazz'),
    path('logout', views.user_logout, name = 'logout'),
    path('automate', views.automate, name = 'automate'),
    path('timetable', views.timetable, name = 'timetable'),
    path('deletettdata/<int:id>', views.deletettdata, name = 'deletettdata'),
    path('autoregister', views.autoregister, name = 'automate register'),
]
