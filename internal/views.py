from django.shortcuts import render, redirect
#from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import User,Student, Teacher, Course

# Create your views here.

def HomePage(request):
    staff = Teacher.objects.filter(userid = '950033')
    print(staff)

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

# for student login he will redirected to student dashboard
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

# for teacher login he will redirected to teacher dashboard
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

# for admin login he will redirected to admin dashboard
def AdminLogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request,'admin_dashboard.html')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request,'logadm.html')

# For every logout
def UserLogout(request):
    logout(request)
    return redirect('home')


def admin_view_course(request):
    return render(request,'admin_view_course.html')

def admin_teacher(request):
    return render(request,'admin_teacher.html')


def admin_student(request):
    return render(request,'admin_student.html')

def add_course(request):
        return render(request,'add_course.html')
 
#for entering course by admin
def submit_form(request):
    current_user = request.user
    if request.method == 'POST':
        # Get form data
        course_code = request.POST['course_id']
        course_name = request.POST['coursename']
        staff_id = request.POST['StaffID']

        # Insert form data into SQLite database
        course = Course.objects.create(course_code = course_code)
        staff = Teacher.objects.get(userid = staff_id)
        course.course_name = course_name
        course.save()
        staff.courses.add(course)
        staff.save()
        messages.success(request, "Course added successfully")
        return render(request, 'add_course.html')

        # Redirect to a new page that will display the form data
        # return render(request,'teacher_course.html', {'courses': courses})
    else:
        return render(request, 'add_course.html')
    
def show_courses(request):
    current_user = request.user
    course_list = (current_user.teacher.courses.all())
    print(course_list)
    return render(request, 'teacher_course.html', {'courses': course_list})


