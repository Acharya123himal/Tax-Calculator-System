from django.urls import include, path
from . import views
from django.contrib.auth import views as auth_views
from .views import ProfileView

urlpatterns = [
    path('',views.getstarted,name="get-started"),
    path('contact/',views.feedback,name="contact"),
    path('about/',views.about,name="about"),
    path('instructions/',views.instructions,name="instructions"),
    path('profile/',ProfileView.as_view(),name="Profile"),
]