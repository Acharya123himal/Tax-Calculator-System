from django.shortcuts import render,HttpResponse,redirect,get_object_or_404,reverse
import requests
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from blog.models import Blog
from authentication.models import User
from django.contrib.auth import get_user_model
user = get_user_model()
from .forms import  MailForm
from .helpers import sendmail
from django.views.generic import ListView

@login_required(login_url = "login")
def dashboard(request):
    data={
        'total_user':len(user.objects.all()),
        'total_active_user':len(user.objects.filter(is_active=True))
        }
    return render(request,"admin/index.html",data)

@login_required(login_url = "login")
def manage_post(request):
    keyword = request.GET.get("keyword")
    if keyword:
        blog = Blog.objects.filter(title__contains = keyword)
        return render(request,"news.html",{"blog":blog})
    blog = Blog.objects.all()
    return render(request,"admin/blog/blog-list.html",{"blog":blog})

@login_required(login_url = "login")
def settings(request):
    return render(request,"admin/settings.html")

@login_required(login_url = "login")
def user_list(request):
    return render(request,"admin/user_list.html",{'users':user.objects.all()})

@login_required(login_url = "login")
def send_mail(request):
    form = MailForm(request.POST or None)
    if form.is_valid():
        formdata = form.save(commit=False)
        sendmail(formdata.sender, formdata.email, formdata.subject, formdata.message)
        messages.success(request,"Mail Sent Successfully")
        return redirect("dashboard")
    return render(request,"admin/send-mail.html",{"form":form})

class MakeAdminView(ListView):
    model=User
    def get(self,request):
        uuser=request.GET.get('username')
        usr = User.objects.get(username=uuser)
        usr.is_staff = True
        usr.is_superuser = True
        usr.save()
        return redirect('user-list')

class DeleteUserView(ListView):
    model=User
    def get(self,request):
        uuser=request.GET.get('username')
        usr = User.objects.get(username=uuser)
        usr.delete()
        return redirect('dashboard')
