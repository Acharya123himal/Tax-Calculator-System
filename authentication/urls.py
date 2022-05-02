from django.urls import include, path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/',views.login_request, name="login"),
    path('logout/',views.logout_request, name="logout"),
    path('signup/',views.register_request, name="register"),
    path('register/',views.register_request, name="register"),
    path('signout/',views.logout_request, name="signout"),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'), 
        name='password_change_done'),

    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html'), 
        name='password_change'),

    path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_done.html'),
    name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html'), name='password_reset'),
    
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
    name='password_reset_complete'),
]
