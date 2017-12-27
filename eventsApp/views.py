from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from django.views import View
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

from .models import Event
from .forms import AddEventForm


login_redirect_url = getattr(settings, 'LOGIN_URL', 'accountsApp:login')
event_shown_per_page = getattr(settings, 'EVENTS_PER_PAGE', 5)

club_name = "EventsClub"
def HasPerm(user):
	return True #user.groups.filter(name=club_name).exists()

# Create your views here.

class EventListView(View):
	def get(self, request, page_num='1'):
		start = ((int(page_num) - 1) * event_shown_per_page)
		next_page = ''
		prev_page = ''
		if Event.objects.all().count() > (start + event_shown_per_page):
			next_page = int(page_num) + 1
		if int(page_num) > 1:
			prev_page = int(page_num) - 1
		context = {
			'latest': Event.objects.order_by('-id')[start:(event_shown_per_page+start)],
			'next_page': next_page,
			'prev_page': prev_page,
			'has_perm': HasPerm(request.user),
		}
		return render(request, 'eventsApp/index.html', context)
	
class DeleteEventView(View):
	def get(self, request, event_id):
		if not HasPerm(request.user):
			return redirect(login_redirect_url)
		get_object_or_404(Event, id=event_id).delete()
		
		return redirect('eventsApp:home')
		
class EventView(View):
	def get(self, request, event_id):
		event = get_object_or_404(Event, id=event_id)
		return render(request, 'eventsApp/event.html', { 'event': event, 'has_perm': HasPerm(request.user) })
		

class AddEventView(View):
	def post(self, request):
		if not HasPerm(request.user):
			return redirect(login_redirect_url)
		
		form = AddEventForm(request.POST)
		if form.is_valid():
			form.save()
		else:
			return render(request, 'eventsApp/addEvent.html', { 'form': form })
		return redirect('eventsApp:home')
	
	def get(self, request):
		if not HasPerm(request.user):
			return redirect(login_redirect_url)
			
		form = AddEventForm()
		return render(request, 'eventsApp/addEvent.html', { 'form': form })
		
class RegisterToEventView(View):
	def get(self, request, event_id, op):
		if not request.user.is_authenticated:
			return redirect(login_redirect_url)
		event = get_object_or_404(Event, id=event_id)
		if op == '0':
			if not request.user in event.usersGoing.all():
				event.usersGoing.add(request.user)
			if request.user in event.usersInterested.all():
				event.usersInterested.remove(request.user)
		elif op == '1':
			if not request.user in event.usersInterested.all():
				event.usersInterested.add(request.user)
			if request.user in event.usersGoing.all():
				event.usersGoing.remove(request.user)
		else:
			if request.user in event.usersGoing.all():
				event.usersGoing.remove(request.user)
			if request.user in event.usersInterested.all():
				event.usersInterested.remove(request.user)
		return redirect('eventsApp:viewEvent', event_id=event_id)
		
class EditEventView(View):
	def post(self, request, event_id):
		if not HasPerm(request.user):
			return redirect(login_redirect_url)
			
		form = AddEventForm(request.POST, instance=get_object_or_404(Event, id=event_id))
		if form.is_valid():
			form.save()
		else:
			return render(request, 'eventsApp/editEvent.html', { 'form': form })
		return redirect('eventsApp:home')
	
	def get(self, request, event_id):
		if not HasPerm(request.user):
			return redirect(login_redirect_url)
			
		form = AddEventForm(instance=get_object_or_404(Event, id=event_id))
		return render(request, 'eventsApp/editEvent.html', { 'form': form })