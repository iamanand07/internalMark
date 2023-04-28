from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    username = models.CharField(max_length=15 ,unique=True)
    is_admin =models.BooleanField('Is Admin', default=False)
    is_student =models.BooleanField('Is Student', default=False)
    is_staff =models.BooleanField('Is Staff', default=False)
    
    def __str__(self):
        return self.username
    
class Teacher(models.Model):
     user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
     userid = models.CharField(max_length=20, null=True)
     name = models.CharField(max_length=60, null=True)
     mobile = models.CharField(max_length=10)
     
     def __str__(self):
        return self.userid
    
    
    
class Student(models.Model):
     user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
     userid = models.CharField(max_length=20, null=True)
     name = models.CharField(max_length=50, null = True)
     mobile = models.CharField(max_length=10)
     
     def __str__(self):
        return self.userid
     
class Subject(models.Model): 
    subject = models.ManyToManyField(Student)
    
    def __str__(self):
        return self.subject
    
     
class Score(models.Model):
    student = models.ForeignKey(User, limit_choices_to={'user_type': 'Student'}, related_name='scored', on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(User, limit_choices_to={'user_type': 'Teacher'}, related_name='marked', on_delete=models.CASCADE)
    exam = models.CharField(max_length=50)
    exam_date = models.DateField()
    score = models.IntegerField()
    out_of = models.IntegerField()
    
    