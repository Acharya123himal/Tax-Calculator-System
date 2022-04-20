from django.shortcuts import render

def getstarted(request):
    return render(request, 'index.html')

def feedback(request):
    return render(request, 'feedback.html')

def about(request):
    return render(request, 'aboutus.html')

def feedback(request):
    return render(request, 'feedback.html')

def instructions(request):
    return render(request, 'howto.html')