from django.urls import include, path
from . import views


urlpatterns = [
    path('calculator/',views.calculator,name='calculator'),
    path('save-calculation/',views.save_calculation,name='save calculation'),
    path('history/',views.history,name='history'),
]