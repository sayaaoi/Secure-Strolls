from django.urls import path 
from . import views  

urlpatterns = [
    path('', views.welcome, name='welcome-page'),
    path('welcome/', views.enterloc, name='welcome-enterlocation'),
]