from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
# class User(AbstractUser):
#     userid = models.CharField(max_length=20 ,unique=True)
#     USERNAME_FIELD = 'userid'
#     REQUIRED_FIELDS = []
#     is_teacher = models.BooleanField(default=False)
#     is_student = models.BooleanField(default=False)
    
    
# class Teacher(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
#     userid = models.CharField(max_length=20, null=True)
#     email = models.EmailField(max_length=200)
#     mobile = models.CharField(max_length=10)
    
    
    
# class Student(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
#     userid = models.CharField(max_length=20, null=True)
#     email = models.EmailField(max_length=200)
#     mobile = models.CharField(max_length=10)


#     # Add the related_name argument to groups and user_permissions fields
#     groups = models.ManyToManyField(
#         Group,
#         verbose_name=_('groups'),
#         blank=True,
#         help_text=_('The groups this user belongs to.'),
#         related_name='internal_users'  # Add related_name argument here
#     )
#     user_permissions = models.ManyToManyField(
#         Permission,
#         verbose_name=_('user permissions'),
#         blank=True,
#         help_text=_('Specific permissions for this user.'),
#         related_name='internal_users'  # Add related_name argument here
#     )