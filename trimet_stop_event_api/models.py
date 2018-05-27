from django.db import models

import django.db.models.options as options
options.DEFAULT_NAMES = options.DEFAULT_NAMES + ('in_db',)

class TrimetStopEvents(models.Model):
    service_date = models.DateField(blank=True, null=True)
    vehicle_number = models.IntegerField(blank=True, null=True)
    train = models.IntegerField(blank=True, null=True)
    route_number = models.IntegerField(blank=True, null=True)
    direction = models.IntegerField(blank=True, null=True)
    trip_number = models.IntegerField(blank=True, null=True)
    service_key = models.TextField(blank=True, null=True)
    stop_time = models.IntegerField(blank=True, null=True)
    arrive_time = models.IntegerField(blank=True, null=True)
    seconds_late = models.IntegerField(blank=True, null=True)
    leave_time = models.IntegerField(blank=True, null=True)
    dwell = models.IntegerField(blank=True, null=True)
    location_id = models.IntegerField(blank=True, null=True)
    door = models.IntegerField(blank=True, null=True)
    lift = models.IntegerField(blank=True, null=True)
    ons = models.IntegerField(blank=True, null=True)
    offs = models.IntegerField(blank=True, null=True)
    estimated_load = models.IntegerField(blank=True, null=True)
    train_mileage = models.FloatField(blank=True, null=True)
    from_location = models.IntegerField(blank=True, null=True)
    mileage_there = models.FloatField(blank=True, null=True)
    left_there = models.IntegerField(blank=True, null=True)
    travel_miles = models.FloatField(blank=True, null=True)
    travel_seconds = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trimet_stop_events'
        in_db = 'trimet_stop_events'
