from django.shortcuts import render
from .models import Meeting, Meeting_Minutes, Resource, Event

# Create your views here.
def index(request):
    return render(request, 'club/index.html')

def meetings(request):
    meeting_title=Meeting.objects.all()
    return render(request, 'club/meetings.html', {'meeting_title': meeting_title})
