from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection
import requests
import json
from django.template.response import TemplateResponse

def welcome(request):
	# function -> Michael
    return render(request, 'welcome/welcome.html')

def enterloc(request):
	req = requests.get("https://maps.googleapis.com/maps/api/directions/json?mode=walking&alternatives=true&origin=202+E+White+St+Champaign+IL&destination=1010+W+Springfield+Ave+Urbana+IL&key=AIzaSyCUV9mE32gI0uU2CpKcYjPXJbXliyTWrKo")
	rjson = req.json()
	routes = rjson["routes"]
# 	for route in routes:
	    
	check = ''
	for route in routes:
		steps = route["legs"][0]["steps"]
		for step in steps:
			s_lat = step["start_location"]["lat"]
			s_long = step["start_location"]["lng"]
			e_lat = step["end_location"]["lat"]
			e_long = step["end_location"]["lng"]
			check = type(s_long)
			if (s_long<e_long):
				s_long -= 0.075
				e_long += 0.075
			else:
				s_long += 0.075
				e_long -= 0.075
				e_long = s_long
				s_long = e_long
				e_long = temp
	        
			if (s_lat < e_lat):
				s_lat -= 0.1125
				e_lat += 0.1125
			else:
				s_lat += 0.1125
				e_lat -= 0.1125
				temp = s_lat
				s_lat = e_lat
				e_lat = temp
	        
			cursor = connection.cursor()
			cursor.execute('SELECT SUM(Score) FROM INCIDENT JOIN Crime WHERE  INCIDENT.Crime_Type = Crime.Crime_Type JOIN LOCATION on INCIDENT.Location.ID = LOCATION.Location_ID WHERE Latitude > {0} and Latitude < {1} and Longitude > {2} and Longitude < {3};'.format(s_lat, e_lat, s_long, e_long))
			rows = cursor.fetchall()
			for row in rows:
				check+= row + "\n"
	        

	arr = [check, 1]
	return TemplateResponse(request, 'welcome/enterloc.html', {"test": arr})

	# context = {
 #        'tests': tests
 #    }
	# return render(request, 'welcome/enterloc.html', {'tests':'Work!'})
# 	return render(request, 'welcome/enterloc.html', test)
    
	# return render(request, 'welcome/enterloc.html', {'che':checkstr})

def result(request):
	return render(request, 'welcome/result.html')


# def myview(request):
#   conn = MySQLdb.connect("connection info here")
#   try:
#     cursor = conn.cursor()
#     cursor.execute("select * from Location")
#     rows = cursor.fetchall()
#   finally:
#     conn.close()

#   return render_to_response("welcome/welcome.html", {"rows" : rows})

