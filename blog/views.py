from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Blog
import requests
from bs4 import BeautifulSoup


def blogView(request):
    response=requests.get('https://english.onlinekhabar.com/wp-json/wp/v2/posts?categories=6').json()
    return render(request, 'news.html',{'response':response})