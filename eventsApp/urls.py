from django.conf.urls import url
from .views import EventListView, EventView, DeleteEventView, AddEventView, EditEventView, RegisterToEventView

app_name = 'eventsApp'
# (?P<page_num>[0-9]+)/
urlpatterns = [
	url(r'^$', EventListView.as_view(), name='home'),
	url(r'^(?P<page_num>[0-9]+)/$', EventListView.as_view(), name='homePage'),
	url(r'^view/(?P<event_id>[0-9]+)/$', EventView.as_view(), name='viewEvent'),
	url(r'^add/$', AddEventView.as_view(), name='addEvent'),
	url(r'^edit/(?P<event_id>[0-9]+)/$', EditEventView.as_view(), name='editEvent'),
	url(r'^delete/(?P<event_id>[0-9]+)/$', DeleteEventView.as_view(), name='deleteEvent'),
	url(r'^reg/(?P<event_id>[0-9]+)/(?P<op>[0-9]+)/$', RegisterToEventView.as_view(), name='regEvent'),
]