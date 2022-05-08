from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.views.generic import ListView
from authentication.models import User
user = get_user_model()

def getstarted(request):
    return render(request, 'index.html')

def feedback(request):
    return render(request, 'feedback.html')

def about(request):
    return render(request, 'aboutus.html')


def instructions(request):
    return render(request, 'howto.html')

# @login_required(login_url = "login")
# def profile(request):
#     if request.method=="POST":
#         user.save()
#         messages.success(request,'Update Successful')
#     return render(request, 'profile.html')


class ProfileView(ListView):
    model=User
    def post(self,request):
        user.address=request.POST.get('address')
        user.first_name=request.POST.get('fname')
        user.last_name=request.POST.get('lname')
        user.username=request.POST.get('username')
        user.gender=request.POST.get('gender')
        user.email=request.POST.get('email')
        user.state=request.POST.get('address')
        user.tel=request.POST.get('tel')
        user.marital=request.POST.get('marital_status')
        user.resident=request.POST.get('resident')
        user.save()
        messages.success(request,'Update Successful')
        return redirect('profile')
    def get(self,request):
        return render(request, 'profile.html')



def page_not_found_view(request,exception):
    return render(request, '404page.html')