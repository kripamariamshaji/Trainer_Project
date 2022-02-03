from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def TRteam(request):
    return render(request, 'Trainer_Team.html')

def Previous(request):
    return render(request, 'Trainer_Previous_Team.html')

def Previous_Task(request):
    return render(request, 'Trainer_Previous_Task.html')

def Previous_Assigned(request):
    return render(request, 'Trainer_Previous_Assigned.html')

def Previous_Trainees(request):
    return render(request, 'Trainer_Previous_Trainees.html')

def Empdetails(request):
    return render(request, 'Trainer_Previous_Empdetails.html')

def Attendance(request):
    return render(request, 'Trainer_Previous_Attendance.html')

def task1(request):
    return render(request, 'Trainer_Previous_Task1.html')

def List(request):
    return render(request, 'Trainer_Previous_Attendance_List.html')

def tdetails(request):
    return render(request, 'Trainer_Previous_Taskdetails.html')

