from django.core.management.base import BaseCommand
from datetime import datetime
from django.db import connection
from bigdataenergy_secure_strolls.models import incidents, location, user

class Command(BaseCommand):
    
    def add_arguments(self, parser):
        parser.add_argument('column', type=str)

    
    def handle(self, *args, **kwargs):
        cursor = connection.cursor()
        column = kwargs['column']
        
        cursor.execute('SELECT {0} FROM LOCATION;'.format(column))
        rows = cursor.fetchall()
        for row in rows:
            print (row)