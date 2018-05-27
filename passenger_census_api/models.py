from django.db import models
from django.contrib.gis.db import models

import django.db.models.options as options
options.DEFAULT_NAMES = options.DEFAULT_NAMES + ('in_db',)

class PassengerCensus(models.Model):
    summary_begin_date = models.DateField(blank=True, null=True)
    route_number = models.IntegerField(blank=True, null=True)
    direction = models.IntegerField(blank=True, null=True)
    service_key = models.TextField(blank=True, null=True)
    stop_seq = models.IntegerField(blank=True, null=True)
    location_id = models.IntegerField(blank=True, null=True)
    public_location_description = models.TextField(blank=True, null=True)
    ons = models.IntegerField(blank=True, null=True)
    offs = models.IntegerField(blank=True, null=True)
    x_coord = models.FloatField(blank=True, null=True)
    y_coord = models.FloatField(blank=True, null=True)
    geom_2913 = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'passenger_census'
        in_db = 'passenger_census'
