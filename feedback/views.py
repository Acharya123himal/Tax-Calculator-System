from django.shortcuts import render
from .models import Feedback
from .form import FeedbackForm
from django.contrib import messages
from django.shortcuts import render,HttpResponse,redirect,get_object_or_404,reverse
from .helpers import send_feedback_mail
from django.contrib.auth.decorators import login_required

def feedback(request):
    form= FeedbackForm(request.POST or None)
    if form.is_valid():
        feedback = form.save(commit=False)
        print(feedback.sender)
        feedback.save()
        try:
            send_feedback_mail(feedback.sender,feedback.tel,feedback.email,feedback.message)
            messages.success(request,'Thank You! Feedback Sent Successfully')
        except:
            pass
        return redirect("feedback")
    return render(request, 'feedback.html')

@login_required(login_url = "login")
def feedback_list(request):
    feedback=Feedback.objects.all()
    print(feedback)
    return render(request,"admin/feedback-list.html",{'feedback':feedback})
