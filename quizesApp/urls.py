from django.conf.urls import url
from .views import QuizesView, DeleteQuizView, QuizResultsView


app_name='quizesApp'

urlpatterns = [
	url(r'^(?P<session_id>[0-9]+)/$', QuizesView.as_view(), name='view'),
	url(r'^delete/(?P<quiz_id>[0-9]+)/$', DeleteQuizView.as_view(), name='delete'),
	url(r'^view/(?P<quiz_id>[0-9]+)/$', QuizResultsView.as_view(), name='results'),
]