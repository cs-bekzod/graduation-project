from django.urls import path
from apps.ishbor.views import index,jobs,job_detail,candidates,ranking,events,event_detail,about,contact,profile

urlpatterns = [
    path('home/', index, name='index'),
    path('jobs/', jobs, name='jobs'),
    path('job-detail/<id>/', job_detail, name='job_detail'),
    path('profile/<id>/', profile, name='profile'),
    path('candidates/', candidates, name='candidates'),
    path('ranking/', ranking, name='ranking'),
    path('events/', events, name='events'),
    path('event-detail/<id>/', event_detail, name='event_detail'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
]