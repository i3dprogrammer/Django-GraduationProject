from django.conf.urls import url
from .views import AddNewQuizView, TestView2, ListQuizesView, DeleteQuizView

app_name = 'onlineExamsApp'

urlpatterns = [
    url(r'^add/(?P<session_id>[0-9]+)$', AddNewQuizView.as_view(), name='add'),
    url(r'^2/$', TestView2.as_view(), name='test2'),
    url(r'^list/(?P<session_id>[0-9]+)$', ListQuizesView.as_view(), name='list'),
    url(r'^delete/(?P<session_id>[0-9]+)/(?P<exam_id>[0-9]+)$',DeleteQuizView.as_view(), name='delete'),
]