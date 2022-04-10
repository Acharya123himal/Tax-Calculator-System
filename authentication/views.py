from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import logout
from .helpers import send_reset_password_mail

def login_request(request):
    if request.method=="POST":
        user=username = password = ''
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/calculator')
        else:
            messages.success(request, 'Invalid credentials.')
            return HttpResponseRedirect('/login')
    else:
        if request.user.is_authenticated:
            return HttpResponseRedirect('/calculator')
        else:
            return render(request, 'login.html')

def logout_request(request):
    logout(request)
    messages.success(request,'Logout Successfully')
    return HttpResponseRedirect('/login')

def register_request(request):
    if request.method=="POST":
        username = password = fname=cpassword=lname=email=''
        username = request.POST.get('username')
        password = request.POST.get('password')
        cpassword = request.POST.get('confirmpassword')
        name=request.POST.get('name')
        name=name.split()
        fname = name[0]
        lname = name[1]
        email = request.POST.get('email')
        if password != cpassword:
            messages.success(request, 'Password not match')
            return HttpResponseRedirect('/signup')
        else:
            user = User.objects.create_user(first_name=fname,last_name=lname,email=email,password=password,username=username)
            if user is not None:
                user.save()
                messages.success(request,'User Created Succefully')
                return HttpResponseRedirect('/login')
            else:
                messages.success(request, 'Please Fill Details Completely')
                return HttpResponseRedirect('/signup')

    else:
        if request.user.is_authenticated:
            return HttpResponseRedirect('/')
        else:
            return render(request, 'signup.html')
