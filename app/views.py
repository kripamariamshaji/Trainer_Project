from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')
def trainer(request):
    return render(request,'trainer.html')
def team(request):
    return render(request,'Trainer_Team.html')
def current(request):
    return render(request,'Trainer_Current_Team.html')
def task(request):
    return render(request,'Trainer_Current_task.html')
def ass(request):
    return render(request,'Trainer_Current_Assigned.html')
def Trainees(request):
    return render(request,'Trainer_Current_Trainees.html')
def Empdetails(request):
    return render(request,'Trainer_Current_Empdetails.html')
def Attendance(request):
    return render(request,'Trainer_Current_Attendance.html')
def task1(request):
    return render(request,'Trainer_Current_task1.html')
def List(request):
    return render(request,'Trainer_Current_AttendanceList.html')
def tdetails(request):
    return render(request,'Trainer_Current_Taskdetails.html')

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

def PEmpdetails(request):
    return render(request, 'Trainer_Previous_Empdetails.html')

def PAttendance(request):
    return render(request, 'Trainer_Previous_Attendance.html')

def Ptask1(request):
    return render(request, 'Trainer_Previous_Task1.html')

def PList(request):
    return render(request, 'Trainer_Previous_Attendance_List.html')

def Ptdetails(request):
    return render(request, 'Trainer_Previous_Taskdetails.html')
