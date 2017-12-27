# uncompyle6 version 2.13.2
# Python bytecode 3.5 (3350)
# Decompiled from: Python 3.5.1 (v3.5.1:37a07cee5969, Dec  6 2015, 01:54:25) [MSC v.1900 64 bit (AMD64)]
# Embedded file name: D:\Programming\DjangoWebsite\HUWebsite\husite\professorsApp\urls.py
# Compiled at: 2017-10-30 06:07:23
# Size of source mod 2**32: 1166 bytes
from django.conf.urls import url
from .views import ProfessorListView, ProfessorView, CourseView, AddProfessorView, EditProfessorView, AddCourseView, EditCourseView, DeleteProfessorView, DeleteCourseView, CourseListView
app_name = 'professorsApp'
urlpatterns = [
	 url('^list/p/$', ProfessorListView.as_view(), name='home'),
	 url('^list/p/(?P<page_num>[0-9]+)/$', ProfessorListView.as_view(), name='homePage'),
	 url('^list/c/(?P<page_num>[0-9]+)/$', CourseListView.as_view(), name='coursePage'),
	 url('^view/p/(?P<prof_id>[0-9]+)/$', ProfessorView.as_view(), name='viewProf'),
	 url('^view/c/(?P<course_id>[0-9]+)/$', CourseView.as_view(), name='viewCourse'),
	 url('^add/p/$', AddProfessorView.as_view(), name='addProf'),
	 url('^add/c/$', AddCourseView.as_view(), name='addCourse'),
	 url('^edit/p/(?P<prof_id>[0-9]+)/$', EditProfessorView.as_view(), name='editProf'),
	 url('^edit/c/(?P<course_id>[0-9]+)/$', EditCourseView.as_view(), name='editCourse'),
	 url('^delete/p/(?P<prof_id>[0-9]+)/$', DeleteProfessorView.as_view(), name='deleteProf'),
	 url('^delete/c/(?P<course_id>[0-9]+)/$', DeleteCourseView.as_view(), name='deleteCourse')
 ]