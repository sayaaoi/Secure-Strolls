from django.db import models

# Create your models here.
# class Location(models.Model):
#     location_id = models.IntegerField(db_column='Location_ID', primary_key=True)  # Field name made lowercase.
#     latitude = models.CharField(db_column='Latitude', max_length=255)  # Field name made lowercase.
#     longitude = models.CharField(db_column='Longitude', max_length=255)  # Field name made lowercase.
#     address = models.TextField(db_column='Address', blank=True, null=True)  # Field name made lowercase.
#     zipcode = models.CharField(db_column='ZipCode', max_length=255, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         # managed = False
#         db_table = 'LOCATION'
