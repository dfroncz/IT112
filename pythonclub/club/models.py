from django.db import models
from django.contrib.auth.models import User
# Create your models here.








class Meeting(models.Model):
    meeting_title=()
    meeting_date=()
    meeting_time=()
    location=()
    agenda=()

    def __str__(self):
        return self.meeting_title
    
    class Meta:
        db_table='Meeting'

class Meeting_Minutes(models.Model):
    meeting_id=()
    attendance=()
    minutes_text=()

    def __str__(self):
        return self.meeting_id

    class Meta:
        db_table='Meeting_Minutes'

class Resource(models.Model):
    resource_name=()
    resource_type=()
    URL=()
    date_entered=()
    user_id=()
    description=()


    def __str__(self):
        return self.resource_name

    class Meta:
        db_table='Resource'

class Event(models.Model):
    event_title=()
    location=()
    date=()
    time=()
    description=()
    user_id=()
    

    def __str__(self):
        return self.event_title

    class Meta:
        db_table='Event'