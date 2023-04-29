from django.shortcuts import render, redirect
#from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import User,Student, Teacher, Subject

# Create your views here.

def HomePage(request):
    return render(request,'home.html')
def SignUpStaff(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        staffname =request.POST['staffname']
        mobile=request.POST['mobilenum']
     
        if password1 == password2:
            is_staff = True
            user = User.objects.create(username=username,first_name=staffname,is_staff = is_staff)
            user.set_password(password1)
            user.save()
            staff = Teacher.objects.create(user = user)
            staff.name = staffname
            staff.userid = username
            staff.mobile = mobile
            staff.save()
            messages.success(request, 'Registration successful! You can now login.')
            return redirect('logfac')
        else:
            messages.error(request, 'Passwords do not match. Please try again.')
    return render(request, 'regfac.html')


def SignUpStudent(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        studentname =request.POST['studentname']
        mobile=request.POST['mobilenum']
     
        if password1 == password2:
            is_student = True
            user = User.objects.create(username=username, first_name = studentname, is_student = is_student)
            user.set_password(password1)
            user.save()
            student = Student.objects.create(user = user)
            student.name = studentname
            student.userid = username
            student.mobile = mobile
            student.save()
            messages.success(request, 'Registration successful! You can now login.')
            return redirect('logstu')
        else:
            messages.error(request, 'Passwords do not match. Please try again.')
    return render(request, 'regstu.html')

def LoginPage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'login.html')

def StudentLogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request,'student_dashboard.html')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request,'logstu.html')


def StaffLogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request,'teacher_dashboard.html')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request,'logfac.html')


def AdminLogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('admin_dashboard')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request,'logadm.html')

