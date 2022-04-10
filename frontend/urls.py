from django.urls import include, path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.getstarted,name="get-started"),
    path('contact/',views.feedback,name="contact"),
    path('about/',views.about,name="about"),
]
