from django.urls import include, path
from . import views

urlpatterns = [
    path('dashboard/',views.dashboard,name = "dashboard"),
    path('blog/addarticle/',views.addBlog,name = "addarticle"),
    path('article/<slug:slug>/',views.detail,name = "detail"),
    path('update/<slug:slug>',views.updateBlog,name = "update"),
    path('delete/<slug:slug>',views.deleteBlog,name = "delete"),
    path('blog/',views.articles,name = "articles"),
]