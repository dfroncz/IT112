from django.test import TestCase
from django.contrib.auth.models import User
from .models import Meeting, Meeting_Minutes, Resource, Event
import datetime
from .forms import MeetingForm
from django.urls import reverse_lazy, reverse

# Create your tests here.
class MeetingTest(TestCase):
    def setUp(self):
        self.type=Meeting(meeting_title='Quarterly')

    def test_typestring(self):
        self.assertEqual(str(self.type), 'Quarterly')

    def test_tablename(self):
        self.assertEqual(str(Meeting._meta.db_table), 'Meeting')

class ResourceTest(TestCase):
    def setUp(self):
        self.resource=Resource(resource_name='Python Tutorial', resource_type='Video', URL='http://linkedin.com', date_entered=datetime.date(2021,6,20), description='Simple python learning method')

    def test_string(self):
        self.assertEqual(str(self.resource), 'Python Tutorial')

class NewMeetingForm(TestCase):
    #valid form data
    def test_meetingform(self):
        data={
                'meeting_title':'Semi',
                'meeting_date':'2021-06-20',
                'meeting_time':'2021-06-20',
                'location': 'Briefing Room',
                'agenda': 'Semi annual meeting',
            }
        form=MeetingForm (data)
        self.assertTrue(form.is_valid)

class New_Meeting_Authentication_Test(TestCase):
    def setUp(self):
        self.test_user=User.objects.create_user(username='testuser1', password='P@ssw0rd1')
        self.meeting=Meeting(meeting_title='Quarterly', meeting_date=datetime.date(2021,6,20), meeting_time=datetime.date(2021,6,20), location='Conference Room', agenda='Discussion of quarterly expectations.')

    def test_redirect_if_not_logged_in(self):
        response=self.client.get(reverse('newmeeting'))
        self.assertRedirects(response, '/accounts/login/?next=/club/newmeeting/')