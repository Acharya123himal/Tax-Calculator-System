from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import logout
from .helpers import send_welcome_mail
from django.views.decorators.cache import cache_control

@cache_control(no_cache=True, must_revalidate=True)
def login_request(request):
    if request.method=="POST":
        user=username = password = ''
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect("/calculator")
        else:
            messages.success(request, 'Invalid credentials.')
            return HttpResponseRedirect("/login/")
    else:
        if request.user.is_authenticated:
            return HttpResponseRedirect("/calculator")
        else:
            return render(request, 'login/login.html')

def logout_request(request):
    logout(request)
    messages.success(request,'Logout Successfully')
    return HttpResponseRedirect("/login/")

def register_request(request):
    if request.method=="POST":
        username = password = fname=cpassword=lname=email=''
        username = request.POST.get('username')
        password = request.POST.get('password')
        cpassword = request.POST.get('confirmpassword')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        if password != cpassword:
            messages.success(request, 'Password not match')
            return HttpResponseRedirect("/register/")
        else:
            user = User.objects.create_user(first_name=fname,last_name=lname,email=email,password=password,username=username)
            if user is not None:
                user.save()
                messages.success(request,'User Created Succefully')
                send_welcome_mail(email, fname)
                return HttpResponseRedirect("/login/")
            else:
                messages.success(request, 'Please Fill Details Completely')
                return HttpResponseRedirect("/register/")

    else:
        if request.user.is_authenticated:
            return HttpResponseRedirect('/')
        else:
            return render(request, 'registration/signup.html')
