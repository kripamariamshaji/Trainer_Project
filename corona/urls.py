"""corona URL Configuration

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
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('trteam', views.TRteam, name='trteam'),
    path('prteam', views.Previous, name='prteam'),
    path('prtask', views.Previous_Task, name='prtask'),
    path('prass', views.Previous_Assigned, name='prass'),
    path('prtrainees', views.Previous_Trainees, name='prtrainees'),
    path('Empdetails', views.Empdetails, name='Empdetails'),
    path('Attendance', views.Attendance, name='Attendance'),
    path('task1', views.task1, name='task1'),
    path('List', views.List, name='List'),
    path('tdetails', views.tdetails, name='tdetails'),
]
