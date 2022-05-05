from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from .helpers import send_feedback_mail
def getstarted(request):
    return render(request, 'index.html')

def feedback(request):
    return render(request, 'feedback.html')

def about(request):
    return render(request, 'aboutus.html')

def feedback(request):
    if request.method=="POST":
        name=request.POST.get('name')
        contact=request.POST.get('contact')
        email=request.POST.get('email')
        message=request.POST.get('message')
        try:
            send_feedback_mail(name,contact,email,message)
            messages.success(request,'Thank You! Feedback Sent Successfully')
        except:
            messages.success(request,'Failed')
        return HttpResponseRedirect('/feedback')
    else:
        return render(request, 'feedback.html')

def instructions(request):
    return render(request, 'howto.html')

def page_not_found_view(request,exception):
    return render(request, '404page.html')