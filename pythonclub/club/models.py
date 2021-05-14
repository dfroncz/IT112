from django.db import models
from django.contrib.auth.models import User
# Create your models here.








class Meeting(models.Model):
    meeting_title=models.CharField(max_length=255, null=True)
    meeting_date=models.DateField(null=True)
    meeting_time=models.DateField(null=True)
    location=models.CharField(max_length=255, null=True)
    agenda=models.TextField(null=True)

    def __str__(self):
        return self.meeting_title
    
    class Meta:
        db_table='Meeting'

class Meeting_Minutes(models.Model):
    meeting_id=models.ForeignKey(Meeting, on_delete=models.DO_NOTHING, null=True)
    attendance=models.ManyToManyField(User)
    minutes_text=models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.meeting_id

    class Meta:
        db_table='Meeting_Minutes'

class Resource(models.Model):
    resource_name=models.CharField(max_length=255, null=True)
    resource_type=models.CharField(max_length=255, null=True)
    URL=models.URLField(null=True)
    date_entered=models.DateField(null=True)
    user_id=models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    description=models.TextField(null=True)


    def __str__(self):
        return self.resource_name

    class Meta:
        db_table='Resource'

class Event(models.Model):
    event_title=models.CharField(max_length=255, null=True)
    location=models.CharField(max_length=255, null=True)
    date=models.DateField(null=True)
    time=models.DateField(null=True)
    description=models.TextField(null=True)
    user_id=models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    

    def __str__(self):
        return self.event_title

    class Meta:
        db_table='Event'