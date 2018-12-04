from django.core.management.base import BaseCommand
from datetime import datetime
from django.db import connection


def handle(self, address, lat, long, location_id, zip):
       
         
    cursor.execute('INSERT INTO LOCATION(Address, Latitude, Longitude, Location_ID, ZipCode) VALUES ({0},{1},{2},{3},{4});'.format(address, lat,long, location_id, zip))