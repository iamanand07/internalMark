"""internalMark URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path,include
from internal import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('',views.HomePage,name='home'),
    path('regfac',views.SignUpStaff,name='regfac'),
    path('regstu',views.SignUpStudent,name='regstu'),
    #path('register',views.SignUpPage,name='register'),
    #path('login',views.LoginPage,name='login'),
    path('logstu',views.StudentLogin,name='logstu'),
    path('logfac',views.StaffLogin,name='logfac'),
    path('logadm',views.AdminLogin,name='logadm'),
    path('student_dashboard',views.StudentLogin,name='student_dashboard'),
    path('teacher_dashboard',views.StaffLogin,name='teacher_dashboard'),
    path('admin_dashboard',views.AdminLogin,name='admin_dashboard'),
    path('logout',views.UserLogout,name='logout'),
    path('admin-view-course',views.admin_view_course,name='admin-view-course'),
    path('admin-teacher',views.admin_teacher,name='admin-teacher'),
    path('admin-student',views.admin_student,name='admin-student'),
    path('add_course',views.submit_form,name='add_course'),
    path('teacher_course',views.show_courses,name='teacher_course')
    # path('teacher_dashboard',views.show_courses,name='teacher_dashboard'),
    
    
    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
