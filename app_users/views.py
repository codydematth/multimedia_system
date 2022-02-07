from django.shortcuts import render, redirect

from app_users.forms import UserForm, UserProfileInfoForm
from .forms import  UserUpdateForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.views.generic import TemplateView
from curriculum.models import Subject
from .models import UserProfileInfo #Contact
# from django.views.generic import CreateView

def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('curriculum:subject_list'))
            else:
                return HttpResponse("ACCOUNT IS DEACTIVATED")
        else:
            return HttpResponse("Please use correct id and password")
            # return HttpResponseRedirect(reverse('register'))

    else:
        return render(request, 'app_users/login.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


# Create your views here.
# def index(request):
#     return render(request,'app_users/index.html')

def register(request):

    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            # user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'app_users/registration.html',
                            {'registered':registered,
                             'user_form':user_form,
                             'profile_form':profile_form})
class HomeView(TemplateView):
    template_name = 'app_users/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        subjects = Subject.objects.all()
        teachers = UserProfileInfo.objects.filter(user_type='teacher')
        context['subjects'] = subjects
        context['teachers'] = teachers
        return context

# class ContactView(CreateView):
#     model = Contact
#     fields = '__all__'
#     template_name = 'app_users/contact.html'

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        

        if u_form.is_valid():
            u_form.save()
           
            # messages.success(request, f'Your profile has been updated!')
            # return redirect('profileview')

    else:
        u_form = UserUpdateForm(instance=request.user)
        

    context = {
        'u_form' : u_form,
        

    }
    return render(request, 'profile.html', context)

# def profile_view(request):

#     return render(request, 'users/profileview.html')