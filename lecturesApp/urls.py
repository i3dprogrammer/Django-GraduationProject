from django.conf.urls import url
from .views import LecturesView, DeleteLectureView

app_name = 'lecturesApp'

urlpatterns =[
    url(r'^(?P<session_id>[0-9]+)/$', LecturesView.as_view(), name='view'),
    url(r'^delete/(?P<lecture_id>[0-9]+)/$', DeleteLectureView.as_view(), name='delete'),
]