from django.urls import include, path
from . import views
from .views import MakeAdminView,DeleteUserView,BlockView,EnableView,RevokeRoleView

urlpatterns = [
    path('dashboard/',views.dashboard,name = "dashboard"),
    path('manage-post/',views.manage_post,name = "manage post"),
    path('settings/',views.settings,name = "settings"),
    path('user-list/',views.user_list,name = "user list"),
    path('block-list/',views.block_list,name = "block list"),
    path('send-mail/',views.send_mail,name = "send mail"),
    path('make-admin/',MakeAdminView.as_view(), name="make admin"),
    path('revoke-admin/',RevokeRoleView.as_view(), name="revoke role"),
    path('delete-user/',DeleteUserView.as_view(), name="delete user"),
    path('block-user/',BlockView.as_view(), name="block user"),
    path('enable-user/',EnableView.as_view(), name="enable user"),
]