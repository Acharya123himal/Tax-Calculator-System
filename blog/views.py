from django.shortcuts import render,HttpResponse,redirect,get_object_or_404,reverse
from django.views.generic import ListView, DetailView
from .models import Blog
import requests
from .forms import BlogForm
from django.contrib import messages
from django.template.defaultfilters import slugify
from django.db.models import Count
from django.contrib.auth.decorators import login_required


def blogView(request):
    response=requests.get('https://english.onlinekhabar.com/wp-json/wp/v2/posts?categories=6').json()
    return render(request, 'onlinekhabar.html',{'blog':response})

def articles(request):
    keyword = request.GET.get("keyword")
    if keyword:
        blog = Blog.objects.filter(title__contains = keyword)
        return render(request,"news.html",{"blog":blog})
    blog = Blog.objects.all()
    return render(request,"news.html",{"blog":blog})

def index(request):
    return render(request,"index.html")
    
def about(request):
    return render(request,"about.html")

@login_required(login_url = "login")
def addBlog(request):
    form = BlogForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        article = form.save(commit=False)
        article.slug = slugify(article.title)
        article.author = request.user
        article.save()
        messages.success(request,"Post Created Successfully")
        return redirect("dashboard")
    return render(request,"admin/blog/add-blog.html",{"form":form})

def detail(request,slug):
    article = get_object_or_404(Blog, slug=slug)
    return render(request,"news_details.html",{"article":article })
    return render(request,"news_details.html",{"blog":article })

@login_required(login_url = "login")
def updateBlog(request, slug):
    article = get_object_or_404(Blog, slug=slug)
    form = BlogForm(request.POST or None,request.FILES or None,instance = article)
    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()
        messages.success(request,"Post has been updated successfully")
        return redirect("dashboard")
    return render(request,"admin/blog/edit-blog.html",{"form":form})

@login_required(login_url = "login")
def deleteBlog(request,slug):
    article = get_object_or_404(Blog,slug=slug)
    article.delete()
    messages.success(request,"Post Successfully Deleted")
    return redirect("dashboard")