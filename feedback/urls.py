from django.urls import include, path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('feedback/',views.feedback,name="feedback"),
    path('feedback-list/',views.feedback_list,name = "feedback list"),
]