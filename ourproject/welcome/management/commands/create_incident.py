from django.core.management.base import BaseCommand
from datetime import datetime
from django.db import connection
from bigdataenergy_secure_strolls.models import incidents, location, user
from datetime import date

class Command(BaseCommand):
    
    def add_arguments(self, parser):
        parser.add_argument('crime_type', type=str)
        parser.add_argument('date', type=str)
        parser.add_argument('description', type=str)
        parser.add_argument('location_id', type = int)
        parser.add_argument('score', type = int)
        parser.add_argument('time', type = str)
        parser.add_argument('incident_id', type=str)

    
    def handle(self, *args, **kwargs):
        cursor = connection.cursor()
        crime_type = '"'+kwargs['crime_type']+'"'
        date_t = kwargs['date'].split('-')
        date_t = date(int(date_t[0]), int(date_t[1]), int(date_t[2])).isoformat()

        description = '"'+ kwargs['description']+'"'
        location_id = kwargs['location_id']
        score = kwargs['score']
        time = '"'+ kwargs['time']+ '"'
        incident_id = '"'+ kwargs['incident_id']+ '"'
         
        cursor.execute('INSERT INTO INCIDENT(Crime_Type, Date, Description, Location_ID, Score, Time, Incident_ID) VALUES ({0},{1},{2},{3},{4},{5}, {6});'.format(crime_type, date_t,description, location_id, score, time, incident_id))