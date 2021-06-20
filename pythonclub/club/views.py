from django.shortcuts import render, get_object_or_404
from .models import Meeting, Meeting_Minutes, Resource, Event
from .forms import MeetingForm

# Create your views here.
def index(request):
    return render(request, 'club/index.html')

def meetings(request):
    meeting_title=Meeting.objects.all()
    return render(request, 'club/meetings.html', {'meeting_title': meeting_title})

def meetingdetail(request, id): 
    meeting=get_object_or_404(Meeting, pk=id)
    return render(request, 'club/meetingdetail.html', {'meeting' : meeting})

def newMeeting(request):
    form=MeetingForm

    if request.method=='POST':
        form=MeetingForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=MeetingForm()
    else:
        form=MeetingForm()
    return render(request, 'club/newmeetingform.html', {'form': form})
