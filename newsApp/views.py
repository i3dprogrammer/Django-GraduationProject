from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from django.views import View
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

from .models import News
from .forms import AddNewsForm


login_redirect_url = getattr(settings, 'LOGIN_URL', 'accountsApp:login')
news_shown_per_page = getattr(settings, 'NEWS_PER_PAGE', 5)

club_name = "NewspaperClub"
def HasPerm(user):
	return user.groups.filter(name=club_name).exists()

# Create your views here.

class NewsHome(View):
	def get(self, request, page_num='1'):
		startNews = ((int(page_num) - 1) * news_shown_per_page)
		next_page = ''
		prev_page = ''
		if News.objects.all().count() > (startNews + news_shown_per_page):
			next_page = int(page_num) + 1
		if int(page_num) > 1:
			prev_page = int(page_num) - 1
		context = {
			'latest_news': News.objects.order_by('-news_date')[startNews:(news_shown_per_page+startNews)],
			'next_page': next_page,
			'prev_page': prev_page,
			'has_perm': HasPerm(request.user),
		}
		return render(request, 'newsApp/index.html', context)
	
class DeleteNewsView(View):
	def get(self, request, news_id):
		if not HasPerm(request.user):
			return redirect(login_redirect_url)
		get_object_or_404(News, id=news_id).delete()
		return redirect('newsApp:NewsHomePage')
		
class NewsArticleView(View):
	def get(self, request, news_id):
		news = get_object_or_404(News, id=news_id)
		return render(request, 'newsApp/article.html', { 'news': news, 'has_perm': HasPerm(request.user) })
		

class AddNewsView(View):
	def post(self, request):
		if not HasPerm(request.user):
			return redirect(login_redirect_url)
		
		news = News(news_date=timezone.now(), user=request.user)
		form = AddNewsForm(request.POST, instance=news)
		if form.is_valid():
			form.save()
		else:
			return render(request, 'newsApp/addNews.html', { 'form': form })
		return redirect('newsApp:NewsHomePage')
	
	def get(self, request):
		if not HasPerm(request.user):
			return redirect(login_redirect_url)
			
		form = AddNewsForm()
		return render(request, 'newsApp/addNews.html', { 'form': form })
		
class EditNewsView(View):
	def post(self, request, news_id):
		if not HasPerm(request.user):
			return redirect(login_redirect_url)
			
		news = News(news_date=timezone.now(), user=request.user)
		form = AddNewsForm(request.POST, instance=get_object_or_404(News))
		if form.is_valid():
			form.save()
		else:
			return render(request, 'newsApp/editNews.html', { 'form': form})
		return redirect('newsApp:NewsHomePage')
	
	def get(self, request, news_id):
		if not HasPerm(request.user):
			return redirect(login_redirect_url)
			
		form = AddNewsForm(instance=get_object_or_404(News, id=news_id))
		return render(request, 'newsApp/editNews.html', { 'form': form})