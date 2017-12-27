from django.conf.urls import url
from .views import TestView, TestView2

app_name = 'onlineExamsApp'

urlpatterns = [
    url(r'^$', TestView.as_view(), name='test'),
    url(r'^2/$', TestView2.as_view(), name='test2'),
]