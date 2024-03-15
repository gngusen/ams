from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Attendance
from .forms import AttendanceForm, LoginForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def view_attendance(request):
    attendances = Attendance.objects.filter(created_date__lte=timezone.now()).order_by('-created_date')
    return render (request, 'attendance/view_attendance.html', {'attendances':attendances})

def new_attendance(request):
    if  request.method == "POST": # If the form has been submitted...
        form = AttendanceForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            attendance = form.save(commit=False)
            attendance.created_date = timezone.now()
            attendance.user = request.user
            attendance.save()
            return view_attendance(request)  
    else:                          
        form = AttendanceForm()   
    return render(request, 'attendance/new_attendance.html', {'form':form})

#login page
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'attendance/login.html', {'form':form})    
        
#logout 
def user_logout(request):
    logout(request)
    return redirect('login')

def home(request):
    return render(request, 'attendance/home.html', {})