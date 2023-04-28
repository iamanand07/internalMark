from django.contrib import admin
from internal.models import User, Student, Teacher, Subject
from django.conf import settings

# Register your models here.

admin.site.register(User)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Subject)
