from django.conf.urls import url

from .views import ProfileHomeView, ScheduleView, OldSemestersView, SessionsView

app_name = 'profileApp'

urlpatterns = [
	url(r'^$', ProfileHomeView.as_view(), name='profile'),
	url(r'^schedule/$', ScheduleView.as_view(), name='schedule'),
	url(r'^semesters/$', OldSemestersView.as_view(), name='semesters'),
	url(r'^sessions/$', SessionsView.as_view(), name='sessions'),
]
