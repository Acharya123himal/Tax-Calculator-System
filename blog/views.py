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
    return render(request, 'news.html',{'response':response})

def articles(request):
    keyword = request.GET.get("keyword")
    if keyword:
        blog = Blog.objects.filter(title__contains = keyword)
        return render(request,"blog.html",{"blog":blog})
    blog = Blog.objects.all()
    return render(request,"news.html",{"blog":blog})

def index(request):
    return render(request,"index.html")
    
def about(request):
    return render(request,"about.html")
@login_required(login_url = "login")
def dashboard(request):
    blog = Blog.objects.filter(author = request.user)
    context = {
        "blog":blog
    }
    return render(request,"admin/blog/blog-list.html",context)

@login_required(login_url = "login")
def addBlog(request):
    form = BlogForm(request.POST or None,request.FILES or None)

    if form.is_valid():
        article = form.save(commit=False)
        article.slug = slugify(article.title)
        article.author = request.user
        article.save()
        messages.success(request,"Makale başarıyla oluşturuldu")
        return redirect("dashboard")
    return render(request,"admin/blog/add-blog.html",{"form":form})

def detail(request,slug):
    #article = Article.objects.filter(id = id).first()   
    article = get_object_or_404(Blog, slug=slug)
    return render(request,"detail.html",{"blog":article })

@login_required(login_url = "login")
def updateBlog(request, slug):
    article = get_object_or_404(Article, slug=slug)
    form = BlogForm(request.POST or None,request.FILES or None,instance = article)
    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()
        messages.success(request,"Makale başarıyla güncellendi")
        return redirect("dashboard")
    return render(request,"update.html",{"form":form})

@login_required(login_url = "login")
def deleteBlog(request,slug):
    article = get_object_or_404(Blog,slug=slug)

    article.delete()

    messages.success(request,"Makale Başarıyla Silindi")

    return redirect("dashboard")