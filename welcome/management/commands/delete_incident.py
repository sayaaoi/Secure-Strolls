from django.core.management.base import BaseCommand
from datetime import datetime
from django.db import connection
# from bigdataenergy_secure_strolls.models import incidents, location, user

class Command(BaseCommand):
    
    def add_arguments(self, parser):
        parser.add_argument('column', type=str)
        parser.add_argument('value', type=str)
    
    def handle(self, *args, **kwargs):
        cursor = connection.cursor()
        column = kwargs['column']
        value = kwargs['value']
        value= '"'+ value+'"'
        
        cursor.execute('DELETE FROM INCIDENT WHERE {0} = {1};'.format(column, value))
        # cursor.execute('DESCRIBE LOCATION');
        # rows = cursor.fetchall()
        # #print(rows)
        # for row in rows:
        #     print(row)