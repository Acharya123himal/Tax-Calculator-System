from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.views.generic import ListView
from authentication.models import User
from authentication.forms import UserForm
user = get_user_model()

def getstarted(request):
    return render(request, 'index.html')

def feedback(request):
    return render(request, 'feedback.html')

def about(request):
    return render(request, 'aboutus.html')

def instructions(request):
    return render(request, 'howto.html')

class ProfileView(ListView):
    model=User
    def post(self,request):
        if not request.user.is_authenticated:
            return redirect('/login')
        details = get_object_or_404(User, username=request.user.username)
        form = UserForm(request.POST or None,instance=details)
        if form.is_valid():
            details = form.save(commit=False)
            details.save()
            messages.success(request,'Profile Update Successful')
        else:
            messages.success(request, 'failed')
        return HttpResponseRedirect('/profile')
    
    def get(self,request):
        if not request.user.is_authenticated:
            return redirect('/login')
        details = get_object_or_404(User, username=request.user.username)
        form = UserForm(request.POST or None,instance=details)
        return render(request, 'profile.html',{"form":form})

def page_not_found_view(request,exception):
    return render(request, '404page.html')