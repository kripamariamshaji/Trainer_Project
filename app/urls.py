from django.contrib import admin
from django.urls import re_path
from app import views

urlpatterns = [
    re_path('admin/', admin.site.urls),
    re_path(r'^$', views.index, name='index'),
    re_path(r'^trainer$', views.Trainers, name='trainer'),
    re_path(r'^trteam$', views.TRteam, name='trteam'),
    re_path(r'^prteam$', views.Previous, name='prteam'),
    re_path(r'^prtask$', views.Previous_Task, name='prtask'),
    re_path(r'^prass$', views.Previous_Assigned, name='prass'),
    re_path(r'^prtrainees$', views.Previous_Trainees, name='prtrainees'),
    re_path(r'^Empdetails$', views.Empdetails, name='Empdetails'),
    re_path(r'^Attendance$', views.Attendance, name='Attendance'),
    re_path(r'^task1$', views.task1, name='task1'),
    re_path(r'^List$', views.List, name='List'),
    re_path(r'^tdetails$', views.tdetails, name='tdetails'),
]
