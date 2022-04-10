from django.urls import include, path
from . import views

from .views import BlogView, ArticleView

urlpatterns = [
    path('blog/',views.blogView),
    # path('blog/',BlogView.as_view(),name='news'),
    # path('blog/post',ArticleView.as_view(),name='article-page')
]
