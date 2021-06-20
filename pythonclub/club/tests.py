from django.test import TestCase
from django.contrib.auth.models import User
from .models import Meeting, Meeting_Minutes, Resource, Event
import datetime

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