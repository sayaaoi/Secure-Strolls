from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection
from .LocationForm import LocationForm
import datetime
import requests
import json
from django.template.response import TemplateResponse
import logging
from requests.utils import unquote 
import re 
import datetime

logger = logging.getLogger(__name__)

def welcome(request):
    return render(request, 'welcome/welcome.html')


def create_request(start_location, end_location):
    # Using GoogleMap API
    final_request = "https://maps.googleapis.com/maps/api/directions/json?mode=walking&alternatives=true&origin="

    start_arr = start_location.split(' ')
    end_arr2 = end_location.split(' ')

    i = 1
    final_request += start_arr[0]
    while i < len(start_arr):
        final_request += "+"+start_arr[i]
        i+=1

    print(final_request)

    final_request += "&destination="

    i = 1
    final_request += end_arr2[0]
    while i < len(end_arr2):
        final_request += "+" + end_arr2[i]
        i += 1
    final_request += "APIKEY"
    return final_request


def enterloc(request):    
    start=None
    arr = []
    stepstring = ""
    routescore  = {}
    rows_saved = []
    last_saved = []
    current_user = request.user
    if (current_user.id != None):
        cursor = connection.cursor()
        cursor.execute("Select start_location, end_location FROM SAVED_ROUTES WHERE saved = 1 and user_id = {0} ORDER BY date_searched DESC".format(current_user.id))
        rows_saved = cursor.fetchall()
        
        cursor = connection.cursor()
    
    try:
        # Using Form
        if request.GET.get('startloc') and request.GET.get('endloc'):             
        # validate_input(start_address, end_address)
                start_location = request.GET.get('startloc')
                end_location = request.GET.get('endloc')
                saved = request.GET.get('saved')
                if (saved == None):
                    saved = 0
                else:
                    saved =1
                if (current_user.id != None):
                    cursor = connection.cursor()
                    start_location = "'"+start_location+"'"
                    end_location = "'" + end_location +"'"
                    cursor.execute('INSERT INTO SAVED_ROUTES(user_id, start_location, end_location, saved) VALUES ({0},{1},{2},{3});'.format(int(current_user.id), str(start_location), str(end_location), saved))


                url = create_request(start_location, end_location)
                req = requests.get(url)
                rjson = req.json()
                routes = rjson["routes"]
                # 	for route in routes:
                checkarr = list()
                check = -1
                check2 = -1
                i = 0

                # Safety score algorithm
                # record score for each route
                scoreDict = dict()
                num_routes = 0
                for route in routes:
                    stepScore = 0
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
                            temp = s_long
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
                        cursor.execute(
                            'SELECT Sum(Score) FROM INCIDENT JOIN Crime ON  INCIDENT.Crime_Type = Crime.Crime_Type JOIN LOCATION ON INCIDENT.Address = LOCATION.Address WHERE Latitude > {0} and Latitude < {1} and Longitude > {2} and Longitude < {3};'.format(
                                s_lat, e_lat, s_long, e_long))
                    
                        # If no crime happens in chosen area, set the value to 0
                        try:
                            cheque = cursor.fetchone()
                            if cheque is None:
                                cheque = (0,)
                            stepScore += list(cheque)[0]
                        except:
                            stepScore += 0

                    routescore[num_routes] = stepScore
                    num_routes +=1;
                sortedRoute = sorted(routescore.items(), key=lambda k:k[1])


                safe_route = routes[sortedRoute[0][0]]
                steps = safe_route["legs"][0]["steps"]
                step_str = list()
                for step in steps:
                    direction = re.sub("<[^>]*>", "", unquote(step["html_instructions"]));
                    distance = " travel " + str(step["distance"]["text"])
                    duration = " for " + str(step["duration"]["text"] + ". ")
                    step_str.append(direction)
                    step_str.append(distance)
                    step_str.append(duration)

                routeText = "You start walking from {0}. Then you need to ".format(start_location)
            
                for move in step_str:
                    routeText += move

                routeText += " Finally you will arrive {0} safely.".format(end_location)

                return TemplateResponse(request, 'welcome/result.html', {"test":routeText, "rows_saved": rows_saved})
           
    except:
        loc_form = LocationForm()
    return TemplateResponse(request, 'welcome/enterloc.html',"rows_saved": rows_saved})
    
def info(reauest):
    cursor = connection.cursor()
    cursor.execute(
        'SELECT Crime_Type, COUNT(Crime_Type) FROM INCIDENT GROUP BY Crime_Type HAVING COUNT(Crime_Type) > 2;')
    val = cursor.fetchall()
    return render(request, 'welcome/info.html',{"crimeNum":val})
    

def result(request):
    return render(request, 'welcome/result.html')
