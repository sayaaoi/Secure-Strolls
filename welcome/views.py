from django.shortcuts import render
from django.http import HttpResponse


def welcome(request):
	# function -> Michael
	return render(request, 'welcome/welcome.html')

def enterloc(request):
 # req = requests.get("https://maps.googleapis.com/maps/api/geocode/json?mode=walking&origin=1600+Amphitheatre+Parkway,+Mountain+View,+CA&key=AIzaSyCUV9mE32gI0uU2CpKcYjPXJbXliyTWrKo")
 #    rjson = req.json()
 #    info = json.loads(json.loads(get_info()))
	test = {'checkstr': "he"}

	# context = {
 #        'tests': tests
 #    }
	# return render(request, 'welcome/enterloc.html', {'tests':'Work!'})
	return render(request, 'welcome/enterloc.html', test)

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

