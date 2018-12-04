from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.welcome, name='welcome-page'),
    path('result/', views.result, name='welcome-result'),
    path('info/', views.result, name='info'),
    path('welcome/', views.enterloc, name='welcome-enterlocation'),
    # path('result/', views.result, name='welcome-result'),
]