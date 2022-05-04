from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render

def admin_check(request):
    return HttpResponseRedirect("/login/")