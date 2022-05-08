from django.urls import include, path
from . import views


urlpatterns = [
    path('dashboard/',views.dashboard,name = "dashboard"),
    path('manage-post/',views.manage_post,name = "manage post"),
    path('settings/',views.settings,name = "settings"),
    path('user-list/',views.user_list,name = "settings"),
]