from unicodedata import name
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    USER = (
        (1,'Admin'),
        (2,'HOD'),
        (3,'Non_Teaching'),
        (4,'Teachers'),
        (5,'Student'),
        (6,'Parent'),
    )
    user_type = models.CharField(choices=USER, max_length=50, default=1)
    profile_pic = models.ImageField(upload_to = 'media/profile_pic')

class Course(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # THIS FUNCTION ARE SHOW COURCE NAME
    def __str__(self):
        return self.name

class Session_Year(models.Model):
    session_start = models.CharField(max_length=100)
    session_end = models.CharField(max_length=100)

    def __str__(self):
        return self.session_start + " to " + self.session_end

# for student pannel


class Student(models.Model):
    # (on_delete variable use for when in student model delete student then it automatically dele student in CustomUser)
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    address = models.TextField()
    gender = models.CharField(max_length=100)
    # only delete on student module
    course_id = models.ForeignKey(Course, on_delete=models.DO_NOTHING)
    session_year_id = models.ForeignKey(Session_Year, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 

    # THIS FUNCTION ARE SHOW admin NAME
    def __str__(self):
        return self.admin.first_name + " " + self.admin.last_name


class Registration(models.Model):
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=12)
    dob = models.DateField()
    mobile_no = models.CharField(max_length=10)
    email = models.EmailField()
    password = models.CharField(max_length=7)
