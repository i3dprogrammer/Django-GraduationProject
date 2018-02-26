from django.conf.urls import url
from .views import HomeView

app_name = 'dashboardApp'
urlpatterns = [
    url(r'^$', HomeView.as_view()),
]