from django.conf.urls import url
from .views import DepartmentsView, DepartmentView

app_name='departmentsApp'

urlpatterns = [
	url(r'^$', DepartmentsView.as_view(), name='departments'),
	url(r'^(?P<group_id>[0-9]+)/$', DepartmentView.as_view(), name='view_department')
]
