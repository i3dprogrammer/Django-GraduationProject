from django.conf.urls import url
from .views import ManageSessionsView, ViewSessionsView

app_name='sessionManagerApp'

urlpatterns = [
	url(r'^manage/$', ManageSessionsView.as_view(), name='manage'),
	url(r'^view/(?P<session_id>[0-9]+)/$', ViewSessionsView.as_view(), name='view'),
]
