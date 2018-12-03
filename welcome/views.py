from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection
import requests
import json
from django.template.response import TemplateResponse
import logging

logger = logging.getLogger(__name__)



def welcome(request):
    return render(request, 'welcome/welcome.html')


def enterloc(request):
    req = requests.get(
        "")
    rjson = req.json()
    routes = rjson["routes"]
    # 	for route in routes:

    checkarr = list()
    check = -1
    check2 = -1
    i = 0
    for route in routes:
        steps = route["legs"][0]["steps"]
        for step in steps:
            s_lat = step["start_location"]["lat"]
            s_long = step["start_location"]["lng"]
            e_lat = step["end_location"]["lat"]
            e_long = step["end_location"]["lng"]
            check = type(s_long)
            if (s_long < e_long):
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

            # cursor = connection.cursor()
            # cursor.execute(
            #     'SELECT Address, Latitude, Longitude, Score FROM INCIDENT JOIN Crime ON  INCIDENT.Crime_Type = Crime.Crime_Type JOIN LOCATION ON INCIDENT.Location_ID = LOCATION.Location_ID;')
            # rows = cursor.fetchall()
            # for row in rows:
            #     checkarr.append(row[0])
            
            cursor = connection.cursor()
            cursor.execute(
                'SELECT Address FROM INCIDENT JOIN Crime ON  INCIDENT.Crime_Type = Crime.Crime_Type JOIN LOCATION ON INCIDENT.Location_ID = LOCATION.Location_ID WHERE Latitude > {0} and Latitude < {1} and Longitude > {2} and Longitude < {3};'.format(
                    s_lat, e_lat, s_long, e_long))
            rows = cursor.fetchall()
            for row in rows:
                checkarr.append(row)

        i += 1
    arr = [check, check2, checkarr]
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

