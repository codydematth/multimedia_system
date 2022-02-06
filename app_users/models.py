from django.db import models
from django.contrib.auth.models import User
import os
from django.urls import reverse

def path_and_rename(instance, filename):
    upload_to = 'Images/'
    ext = filename.split('.')[-1]
    # get filename
    if instance.pk:
        filename = 'User_Profile_Pictures/{}.{}'.format(instance.pk, ext)
    return os.path.join(upload_to, filename)

class UserProfileInfo(models.Model):

    #creating a relationship with user class (not inheriting)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #adding additional attributes
    
    profile_pic = models.ImageField(upload_to=path_and_rename, verbose_name="Profile Picture", blank=True)
    teacher = 'teacher'
    student = 'student'
    jss1 = 'jss1'
    jss2 = 'jss2'
    jss3 = 'jss3'
    sss1 = 'sss1'
    sss2 = 'sss2'
    sss3 = 'sss3'
    # parent = 'parent'
    user_types = [
        (teacher, 'teacher'),
        (student, 'student'),
        # (parent, 'parent'),
    ]
    user_type = models.CharField(max_length=10, choices=user_types, default=student)
    
    levels = [
        (jss1, 'jss1'),
        (jss2, 'jss2'),
        (jss3 , 'jss3'),
        (sss1 , 'sss1'),
        (sss2 , 'sss2'),
        (sss3 , 'sss3'),
    ]
    
    level = models.CharField(max_length=10, choices=levels, default=jss1)

    def __str__(self):
        return self.user.username

