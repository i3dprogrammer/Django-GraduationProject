from django.conf.urls import url
from .views import LoginView, RegisterStudentView, RegisterProfessorView, LogoutView

app_name='accountsApp'

urlpatterns = [
	url(r'^$', LoginView.as_view(), name='login'),
	url(r'^logout/$', LogoutView.as_view(), name='logout'),
	url(r'^reg/s/$', RegisterStudentView.as_view(), name='regStudent'),
	url(r'^reg/p/$', RegisterProfessorView.as_view(), name='regProf'),
]