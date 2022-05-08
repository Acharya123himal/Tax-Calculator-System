from django.urls import include, path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('blog/addarticle/',views.addBlog,name = "addarticle"),
    path('blog/article/<slug:slug>/',views.detail,name = "detail"),
    path('update/<slug:slug>',views.updateBlog,name = "update"),
    path('delete/<slug:slug>',views.deleteBlog,name = "delete"),
    path('blog/',views.articles,name = "articles"),
    path('update/<slug:slug>',views.updateBlog,name = "update"),
]
# urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
