from django.shortcuts import render, redirect, get_object_or_404
#from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import User, Student, Teacher, Course, Mark

# Create your views here.

def HomePage(request):
    return render(request,'home.html')
   
    
def aboutUs(request):
    return render(request,'aboutUs.html')
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
 
#for entering course by admin for teacher
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
    else:
        return render(request, 'add_course.html')
    
    
    
#display the taken course for teacher
def show_courses(request):
    current_user = request.user
    course_list = (current_user.teacher.courses.all())
    print(course_list)
    return render(request, 'teacher_course.html', {'courses': course_list})



#display the taken course for student
def show_courses_student(request):
    current_user = request.user
    course_list = (current_user.student.courses.all())
    print(course_list)
    return render(request, 'student_course.html', {'courses': course_list})

#after click the href link in the teacher course it will return the mark html page

def courseclick(request):
    return render(request,'add_marks.html')

def admin_dashboard_view(request):
    dict={
    'total_student':Student.objects.all().count(),
    'total_teacher':Teacher.objects.all().filter(status=True).count(),
    'total_course':Course.objects.all().count(),
    }
    return render(request,'admin_dashboard.html',context=dict)
  


#for entering marks for the student by teacher
def enter_marks(request):
    if request.method == 'POST':
        student_id = request.POST['student_id']
        course_code = request.POST['course_code']
        internal1 =request.POST['internal1']
        internal2 =request.POST['internal2']
        internal3 =request.POST['internal3']
        attendance1=request.POST['attendance1']
        attendance2=request.POST['attendance2']
        attendance3=request.POST['attendance3']
        # Get the student and course objects
        student = get_object_or_404(Student, userid=student_id)
        course = get_object_or_404(Course, course_code=course_code)
            
        # Create or update the mark
        mark, created = Mark.objects.update_or_create(
            student=student,
            course=course,
            defaults={
                    'internal1': internal1,
                    'internal2': internal2,
                    'internal3': internal3,
                    'attendance1': attendance1,
                    'attendance2': attendance2,
                    'attendance3': attendance3
                }
            )
            # Optionally, you can perform any additional actions or redirect to a success page
            # For simplicity, we'll just render a success message
        return render(request, 'add_marks.html', {'message': 'Marks entered successfully!'})
    else:
        return render(request, 'add_marks.html')


def student_marks(request):
    current_user = request.user
    student = Student.objects.filter(userid = current_user.student.userid)
    mark = (Mark.objects.filter(student_id = current_user.student.user_id))
    
    return render(request, 'student_marks.html', {'student': student, 'marks': mark})
   





