from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    username = models.CharField(max_length=15 ,unique=True)
    is_admin =models.BooleanField('Is Admin', default=False)
    is_student =models.BooleanField('Is Student', default=False)
    is_staff =models.BooleanField('Is Staff', default=False)
    
    def __str__(self):
        return self.username
    


class Course(models.Model): 
    course_name = models.CharField(max_length=60)
    course_code = models.CharField(max_length=10,unique=True)
    
     
    def __str__(self):
        return self.course_code
    

class Student(models.Model):
     user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
     userid = models.CharField(max_length=20, null=True)
     name = models.CharField(max_length=50, null = True)
     mobile = models.CharField(max_length=10)
     courses = models.ManyToManyField(Course)
     
     
     def __str__(self):
        return self.userid

     
    
    
class Teacher(models.Model):
     user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
     userid = models.CharField(max_length=20, null=True)
     name = models.CharField(max_length=60, null=True)
     mobile = models.CharField(max_length=10)
     courses = models.ManyToManyField(Course)
     
     def __str__(self):
        return self.userid
    
    
     
class Mark(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    internal1 = models.IntegerField()
    internal2 = models.IntegerField()
    internal3 = models.IntegerField()
    attendance1 = models.IntegerField()
    attendance2 = models.IntegerField()
    attendance3 = models.IntegerField()
    
    def __str__(self):
        return self.student.name
    
    
     
     
     