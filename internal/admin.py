from django.contrib import admin
from internal.models import User, Student, Teacher, Course, Mark
from django.conf import settings

# Register your models here.

admin.site.register(User)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Course)
admin.site.register(Mark)
