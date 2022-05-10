from django.shortcuts import render,redirect,get_object_or_404,reverse
import requests
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from blog.models import Blog
from .models import Settings
from feedback.models import Feedback
from calculator.models import TaxCalculator
from authentication.models import User
from django.contrib.auth import get_user_model
user = get_user_model()
from .forms import  MailForm, SettingsForm
from .helpers import sendmail
from django.views.generic import ListView
from django.core.cache import cache

@login_required(login_url = "login")
def dashboard(request):
    if not request.user.is_staff:
        return HttpResponseRedirect('/calculator')
    data={
        'total_user':len(user.objects.all()),
        'total_active_user':len(user.objects.filter(is_active=True)),
        'total_feedback':len(Feedback.objects.all()),
        'total_blacklist':len(user.objects.filter(is_blocked=True)),
        'total_calculation':len(TaxCalculator.objects.all()),
        }
    return render(request,"admin/index.html",data)

@login_required(login_url = "login")
def manage_post(request):
    if not request.user.is_staff:
        return HttpResponseRedirect('/calculator')
    keyword = request.GET.get("keyword")
    if keyword:
        blog = Blog.objects.filter(title__contains = keyword)
        return render(request,"news.html",{"blog":blog})
    blog = Blog.objects.all()
    return render(request,"admin/blog/blog-list.html",{"blog":blog})

class SettingsView(ListView):
    def get(self,request):
        if not request.user.is_staff:
            return HttpResponseRedirect('/calculator')
        # article = get_object_or_404(Settings, logo="logo.png")
        form = SettingsForm(request.POST or None)
        return render(request,"admin/settings.html",{"form":form})
    def post(self,request):
        if not request.user.is_staff:
            return HttpResponseRedirect('/calculator')
        form = SettingsForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            formdata = form.save(commit=False)
            formdata.save()
            messages.success(request,"Logo Updated Successfully")
            cache.clear()
            return HttpResponseRedirect("/settings")
        return render(request,"admin/settings.html",{"form":form})
    
@login_required(login_url = "login")
def user_list(request):
    if not request.user.is_staff:
        return HttpResponseRedirect('/calculator')
    return render(request,"admin/user_list.html",{'users':user.objects.all()})

@login_required(login_url = "login")
def block_list(request):
    if not request.user.is_staff:
        return HttpResponseRedirect('/calculator')
    return render(request,"admin/block_list.html",{'users':user.objects.filter(is_blocked=True)})

@login_required(login_url = "login")
def send_mail(request):
    if not request.user.is_staff:
        return HttpResponseRedirect('/calculator')
    form = MailForm(request.POST or None)
    if form.is_valid():
        formdata = form.save(commit=False)
        sendmail(formdata.sender, formdata.email, formdata.subject, formdata.message)
        messages.success(request,"Mail Sent Successfully")
        return HttpResponseRedirect("dashboard/")
    return render(request,"admin/send-mail.html",{"form":form})

class MakeAdminView(ListView):
    model=User
    def get(self,request):
        if not request.user.is_staff:
            return HttpResponseRedirect('/calculator')
        uuser=request.GET.get('username')
        usr = User.objects.get(username=uuser)
        usr.is_staff = True
        usr.is_superuser = True
        usr.save()
        return HttpResponseRedirect('/user-list/')
    
class RevokeRoleView(ListView):
    model=User
    def get(self,request):
        if not request.user.is_staff:
            return HttpResponseRedirect('/calculator')
        uuser=request.GET.get('username')
        usr = User.objects.get(username=uuser)
        usr.is_staff = False
        usr.is_superuser = False
        usr.save()
        return HttpResponseRedirect('/user-list/')
    
class BlockView(ListView):
    model=User
    def get(self,request):
        if not request.user.is_staff:
            return HttpResponseRedirect('/calculator')
        uuser=request.GET.get('username')
        usr = User.objects.get(username=uuser)
        usr.is_blocked = True
        usr.is_active = False
        usr.save()
        return HttpResponseRedirect('/user-list/')
    
class EnableView(ListView):
    model=User
    def get(self,request):
        if not request.user.is_staff:
            return HttpResponseRedirect('/calculator')
        uuser=request.GET.get('username')
        usr = User.objects.get(username=uuser)
        usr.is_blocked = False
        usr.is_active = True
        usr.save()
        return HttpResponseRedirect('/user-list/')

class DeleteUserView(ListView):
    model=User
    def get(self,request):
        if not request.user.is_staff:
            return HttpResponseRedirect('/calculator')
        uuser=request.GET.get('username')
        usr = User.objects.get(username=uuser)
        usr.delete()
        return HttpResponseRedirect('dashboard/')
