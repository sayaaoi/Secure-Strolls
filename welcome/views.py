from django.shortcuts import render
from django.http import HttpResponse

def welcome(request):
    return HttpResponse('<h1>Welcome!</h1>')

