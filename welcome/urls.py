from django.urls import path 
from . import views  

urlpatterns = [
    path('', views.welcome, name='welcome-page'),
    path('result/', views.result, name='welcome-result'),
    path('welcome/', views.enterloc, name='welcome-enterlocation'),
    # path('result/', views.result, name='welcome-result'),
]