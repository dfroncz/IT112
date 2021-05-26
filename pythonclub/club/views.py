from django.shortcuts import render, get_object_or_404
from .models import Meeting, Meeting_Minutes, Resource, Event

# Create your views here.
def index(request):
    return render(request, 'club/index.html')

def meetings(request):
    meeting_title=Meeting.objects.all()
    return render(request, 'club/meetings.html', {'meeting_title': meeting_title})

def meetingdetail(request, id): 
    meeting=get_object_or_404(Meeting, pk=id)
    return render(request, 'club/meetingdetail.html', {'meeting' : meeting})
