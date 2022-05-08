from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
user = get_user_model()

def getstarted(request):
    return render(request, 'index.html')

def feedback(request):
    return render(request, 'feedback.html')

def about(request):
    return render(request, 'aboutus.html')


def instructions(request):
    return render(request, 'howto.html')

@login_required(login_url = "login")
def profile(request):
    if request.method=="POST":
        user.address="Ghodaghodi"
        # user.first_name
        # user.last_name
        # user.username
        # user.gender
        # user.email
        # user.state
        # user.tel
        user.save()
        messages.success(request,'Update Successful')
    return render(request, 'profile.html')

def page_not_found_view(request,exception):
    return render(request, '404page.html')