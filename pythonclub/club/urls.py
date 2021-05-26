from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('meetings/', views.meetings, name='meetings'),
    path('meetingdetail/<int:id>', views.meetingdetail, name='detail'),
]