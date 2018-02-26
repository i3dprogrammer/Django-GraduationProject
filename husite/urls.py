"""husite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
	url(r'^news/', include('newsApp.urls')),
	url(r'^professors/', include('professorsApp.urls')),
	url(r'^events/', include('eventsApp.urls')),
	url(r'^', include('accountsApp.urls')),
	url(r'^sessions/', include('sessionManagerApp.urls')),
	url(r'^profile/', include('profileApp.urls')),
    url(r'^courses/', include('coursesApp.urls')),
    url(r'^departments/', include('departmentsApp.urls')),
    url(r'^quizes/', include('quizesApp.urls')),
    url(r'^lectures/', include('lecturesApp.urls')),
    url(r'exam/', include('onlineExamsApp.urls')),
    url(r'dashboard/', include('dashboard.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)