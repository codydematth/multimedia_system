from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from app_users.models import UserProfileInfo

class UserForm(UserCreationForm):
    email = forms.EmailField()

    class Meta():
        model = User
        fields = ('username','first_name','last_name', 'email', 'password1', 'password2')

        # widgets = {
        # "password":"forms.PasswordInput()",
        # }

        labels = {
        'password1':'Password',
        'password2':'Confirm Password'
        }

class UserProfileInfoForm(forms.ModelForm):
    # teacher = 'teacher'
    # student = 'student'
    
    # jss1 = 'jss1'
    # jss2 = 'jss2'
    # jss3 = 'jss3'
    # sss1 = 'sss1'
    # sss2 = 'sss2'
    # sss3 = 'sss3'
    # # parent = 'parent'
    # user_types = [
    #     (student, 'student'),
    #     # (teacher, 'teacher'),
    # ]
    # user_type = forms.ChoiceField(required=True, choices=user_types)
    
    # levels = [
    #     (jss1, 'jss1'),
    #     (jss2, 'jss2'),
    #     (jss3 , 'jss3'),
    #     (sss1 , 'sss1'),
    #     (sss2 , 'sss2'),
    #     (sss3 , 'sss3'),
    # ]
    
    # level = forms.ChoiceField(required=True, choices=levels)


    class Meta():
        model = UserProfileInfo
        fields = ['profile_pic']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(max_length=60, help_text='Required. Add a valid email address')

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = UserProfileInfo
		fields = ['profile_pic']