from django.shortcuts import render
from django.http import HttpResponse

def welcome(request):
    return render(request, 'welcome/welcome.html')

def enterloc(request):
	return render(request, 'welcome/enterloc.html')

