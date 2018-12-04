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
    final_request = "https://maps.googleapis.com/maps/api/directions/json?mode=walking&alternatives=true&origin="

    # final_request = url+"mode=walking&alternatives=true&"+"origin="
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
    final_request += "&key=AIzaSyCUV9mE32gI0uU2CpKcYjPXJbXliyTWrKo"
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
        
        # for row in row
        # rows_saved_clean = rows_saved[0]
        
        cursor = connection.cursor()
        # cursor.execute("Select start_location, end_location, MAX(date_searched) FROM SAVED_ROUTES WHERE user_id = {0}".format(current_user.id))
        # q = "Select DISTINCT start_location, end_location FROM SAVED_ROUTES WHERE user_id = {0} and date_searched = (Select MAX(date_searched) FROM SAVED_ROUTES)".format(current_user.id)
        # cursor.execute(q)
        # last_saved = cursor.fetchall()[0]
        
        # last_saved_clean = last_saved[0]
        # for route in last_saved[0]:
        #     last_saved_clean = route
            # if type(route) is str:
            #     last_saved_clean += route
            # else:
            #     last_saved_clean += route.strftime('%m/%d/%Y')
        
    
    # if request.user.is_authenticated():
    # # Do something for authenticated users.
    #     checkuser = str(current_user.id)
    # else:
    # # Do something for anonymous users.
    #     checkuser = "rip"
    # if request.GET.get('startloc'):
    #     startloc = request.GET.get('startloc')
    #     endloc = request.GET.get('endloc')
    #     startloc.save()
    #     endloc.save()
    #     arr = [startloc, endloc]
    #     # locs = {'startloc':startloc, 'endloc':endloc}
    # return render(request, 'welcome/enterloc.html', {'locs': arr})
       
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
                
                
            #     cursor.execute('INSERT INTO SAVED_ROUTES (user_id, start_location, end_location, saved) VALUES ('+str(current_user.id) +',' + start_location + ','+end_location + ','+str((saved != None))+');')
                
                # cursor.execute('INSERT INTO SAVED_ROUTES (user_id, start_location, end_location, saved) VALUES ({0}, {1}, {2}, {3});'.format(int(current_user.id), start_location), str(end_location), (saved != None)))
            url = create_request(start_location, end_location)
            req = requests.get(url)
            # req = requests.get(
            #     "https://maps.googleapis.com/maps/api/directions/json?mode=walking&alternatives=true&origin=202+E+White+St+Champaign+IL&destination=1010+W+Springfield+Ave+Urbana+IL&key=AIzaSyCUV9mE32gI0uU2CpKcYjPXJbXliyTWrKo")
            
            rjson = req.json()
            routes = rjson["routes"]
            # 	for route in routes:
            checkarr = list()
            check = -1
            check2 = -1
            i = 0
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
                            
                    # cursor.execute(
                    #     'SELECT SUM(Score) FROM INCIDENT JOIN Crime ON  INCIDENT.Crime_Type = Crime.Crime_Type JOIN LOCATION ON INCIDENT.Location_ID = LOCATION.Location_ID' )
                    
                    # try:
                    #     cheque = cursor.fetchall()
                    #     for row in cheque:
                    #         if cheque is None or row is None:
                    #             row = (0,"")
                    #         stepstring += row[0]+ " "+ row[1]
                    #         # stepScore += list(cheque)[0]
                    # except:
                    #     stepScore = 0
                    try:
                        cheque = cursor.fetchone()
                        if cheque is None:
                            cheque = (0,)
                        # stepstring += cheque[0]+ " "+ cheque[1]
                        stepScore += list(cheque)[0]
                    except:
                        stepScore += 0
                    
                    # cursor.execute(
                    #     'SELECT Address FROM INCIDENT JOIN Crime ON  INCIDENT.Crime_Type = Crime.Crime_Type JOIN LOCATION ON INCIDENT.Location_ID = LOCATION.Location_ID WHERE Latitude > {0} and Latitude < {1} and Longitude > {2} and Longitude < {3};'.format(
                    #         s_lat, e_lat, s_long, e_long))
                            
                    # A list of addresses
                    # stepAddress = cursor.fetchall()
                # i += 1
                # index = 'Route' + i
                # scoreDict[index] = [stepScore, stepAddress]
            # Find the safest route based on score
                routescore[num_routes] = stepScore
                num_routes +=1;
            sortedRoute = sorted(routescore.items(), key=lambda k:k[1])
            # bestRoute = sortedRoute[0][1][1]
            # bestRoute = url
            # arr = [check, check2, checkarr]
            # sortedroutescore = sorted(routescore)
            
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
            
            # return TemplateResponse(request, 'welcome/result.html', {"test2":str(saved)})
            return TemplateResponse(request, 'welcome/result.html', {"test":routeText, "rows_saved": rows_saved})
            # return TemplateResponse(request, 'welcome/result.html', {"test":routeText, "rows_saved": rows_saved, "last_saved": last_saved})
    else:
        loc_form = LocationForm()
    return TemplateResponse(request, 'welcome/enterloc.html',{'warning': "Please type in addresses!", "rows_saved": rows_saved})
    
def info(reauest):
    cursor = connection.cursor()
    cursor.execute(
        'SELECT Crime_Type, COUNT(Crime_Type) FROM INCIDENT GROUP BY Crime_Type HAVING COUNT(Crime_Type) > 2;')
    val = cursor.fetchall()
    return render(request, 'welcome/info.html',{"crimeNum":val})
    

def result(request):
    # current_user = request.user
    # if (current_user.id != None):
    #     cursor = connection.cursor()
    #      cursor.execute('INSERT INTO SAVED_ROUTES (user_id, start_location, end_location, saved) VALUES ({0}, {1}, {2}, {3});'.format(curent_user.id, start_location, end_location, (saved != None)))
    return render(request, 'welcome/result.html')


                    # cursor = connection.cursor()
                    # cursor.execute(
                    #     'SELECT Address, Latitude, Longitude, Score FROM INCIDENT JOIN Crime ON  INCIDENT.Crime_Type = Crime.Crime_Type JOIN LOCATION ON INCIDENT.Location_ID = LOCATION.Location_ID;')
                    # rows = cursor.fetchall()
                    # for row in rows:
                    #     checkarr.append(row[0])
                    
                    
                    # cursor.execute(
                    #     'SELECT Score FROM INCIDENT JOIN Crime ON  INCIDENT.Crime_Type = Crime.Crime_Type JOIN LOCATION ON INCIDENT.Location_ID = LOCATION.Location_ID WHERE Latitude > {0} and Latitude < {1} and Longitude > {2} and Longitude < {3};'.format(
                    #         s_lat, e_lat, s_long, e_long))                    
                    

        #if request.method == 'POST':
        # loc_form = LocationForm(request.POST)
        # if loc_form.is_valid():
        #     start_loc = loc_form.cleaned_data['start']
        #     end_loc = loc_form.cleaned_data['end']
            # loc_form.save()
            # start_loc = loc_form.cleaned_data.get('start')
            # end_loc = loc_form.cleaned_data.get('end')
            # arr =[start_loc, end_loc]
            # args = {'loc_form': loc_form, 'start_loc':start_loc, 'start_loc':end_loc}
    
    
    # return render(request, 'welcome/enterloc.html', {'locs': arr})