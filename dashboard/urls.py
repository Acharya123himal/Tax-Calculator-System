from django.urls import include, path
from . import views
from .views import MakeAdminView,DeleteUserView

urlpatterns = [
    path('dashboard/',views.dashboard,name = "dashboard"),
    path('manage-post/',views.manage_post,name = "manage post"),
    path('settings/',views.settings,name = "settings"),
    path('user-list/',views.user_list,name = "user list"),
    path('send-mail/',views.send_mail,name = "send mail"),
    path('make-admin/',MakeAdminView.as_view(), name="make admin"),
    path('delete-user/',DeleteUserView.as_view(), name="delete user"),
]