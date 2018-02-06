from django.conf.urls import url
from .views import ManageSessionsView, ViewSessionsView, DropSessionView, DropSession, TestingView

app_name='sessionManagerApp'

urlpatterns = [
	url(r'^manage/$', ManageSessionsView.as_view(), name='manage'),
	url(r'^view/(?P<session_id>[0-9]+)/$', ViewSessionsView.as_view(), name='view'),
	url(r'^drop/view/(?P<session_id>[0-9]+)/$', DropSessionView.as_view(), name='drop_view'),
	url(r'^drop/(?P<session_id>[0-9]+)/$', DropSession.as_view(), name='drop'),
	url(r'^(?P<session_id>[0-9]+?)/$', TestingView.as_view(), name='test')
]
