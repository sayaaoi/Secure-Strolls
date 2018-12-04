from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.welcome2, name='welcome2-page'),
    path('result2/', views.result, name='welcome2-result'),
    path('welcome2/', views.enterloc, name='welcome2-enterlocation'),
    # path('result/', views.result, name='welcome-result'),
]