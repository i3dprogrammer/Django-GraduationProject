from django.conf.urls import url
from .views import NewsHome, NewsArticleView, AddNewsView, EditNewsView, DeleteNewsView

app_name='newsApp'

urlpatterns = [
	url(r'^$', NewsHome.as_view(), name='NewsHomePage'),
    url(r'^(?P<page_num>[0-9]+)/$', NewsHome.as_view(), name='NewsPage'),
	url(r'^view/(?P<news_id>[0-9]+)/$', NewsArticleView.as_view(), name='newsArticle'),
	url(r'^delete/(?P<news_id>[0-9]+)/$', DeleteNewsView.as_view(), name='deleteNews'),
	url(r'^add/$', AddNewsView.as_view(), name='addNews'),
	url(r'^edit/(?P<news_id>[0-9]+)/$', EditNewsView.as_view(), name='editNews'),
]
