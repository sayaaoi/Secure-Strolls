from django.core.management.base import BaseCommand
from datetime import datetime
from django.db import connection

class Command(BaseCommand):
    
    def add_arguments(self, parser):
        # parser.add_argument('update_column', type=str)
        # parser.add_argument('update_value', type=str)
        # parser.add_argument('column', type=str)
        # parser.add_argument('value', type=str)
        parser.add_argument('update_column')
        parser.add_argument('update_value')
        parser.add_argument('column')
        parser.add_argument('value')
    
    def handle(self, *args, **kwargs):
        cursor = connection.cursor()
        update_column = kwargs['update_column']
        update_value = kwargs['update_value']
        update_value = '"'+update_value+'"'
        column = kwargs['column']
        value = kwargs['value']
        value = '"'+value+'"'
        
        stri = 'UPDATE INCIDENT SET {0}={1} WHERE {2}={3};'.format(update_column, update_value, column, value)
        print(stri)
        cursor.execute(stri)
        #cursor.execute('UPDATE INCIDENT SET Crime_Type="MURDER" WHERE Description="BATTERY";')