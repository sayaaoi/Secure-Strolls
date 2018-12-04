from django.shortcuts import render
from django.http import HttpResponse
import requests
import json

def welcome(request):
    return render(request, 'welcome/welcome.html')

def enterloc(request):
	return render(request, 'welcome/enterloc.html')

def result(request):
	return render(request, 'result.html')


# def myview(request):
#   conn = MySQLdb.connect("connection info here")
#   try:
#     cursor = conn.cursor()
#     cursor.execute("select * from Location")
#     rows = cursor.fetchall()
#   finally:
#     conn.close()

#   return render_to_response("welcome/welcome.html", {"rows" : rows})

