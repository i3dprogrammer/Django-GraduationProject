from django.conf.urls import url
from .views import CoursesViewVersion2, CourseView

app_name='coursesApp'

urlpatterns = [
	url(r'^$', CoursesViewVersion2.as_view(), name='courses'),
	url(r'^(?P<course_id>[0-9]+)/$', CourseView.as_view(), name='view_course'),
]
