from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, UserForm, RegisterProfessorForm
from django.views import View
from django.http import HttpResponse
# Create your views here.

home_redirect_url = getattr(settings, 'HOME_URL', 'profileApp:profile')
login_redirect_url = getattr(settings, 'LOGIN_URL', 'accountsApp:login')

club_name = "RegistrationClub"
def HasPerm(user):
	return True #user.groups.filter(name=club_name).exists()

class LoginView(View):
	def post(self, request):
		if request.user.is_authenticated:
			return redirect(home_redirect_url)
			
		form = LoginForm(request.POST)
		if form.is_valid():
			user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
			if user is not None:
				login(request, user)
			else:
				form.add_error('', 'Invalid username and/or password!')
				return render(request, 'accountsApp/login.html', { 'form':form })		
		else:
			return render(request, 'accountsApp/login.html', { 'form':form })	
			
		return redirect(home_redirect_url)
		
	def get(self, request):
		if request.user.is_authenticated:
			return redirect(home_redirect_url)
			
		form = LoginForm()
		return render(request, 'accountsApp/login.html', { 'form':form })
		
class LogoutView(View):
	def get(self, request):
		if request.user.is_authenticated:
			logout(request)
		
		return redirect(login_redirect_url)

class RegisterStudentView(View):
	def post(self, request):
		if not HasPerm(request.user):
			return redirect(login_redirect_url)
		
		form = UserForm(request.POST)
		if form.is_valid():
			form.save()
		else:
			return render(request, 'accountsApp/regStudent.html', { 'form':form })
			
		return redirect(home_redirect_url)
		
	def get(self, request):
		if not HasPerm(request.user):
			return redirect(login_redirect_url)
		
		form = UserForm()
		return render(request, 'accountsApp/regStudent.html', { 'form':form })
		
class RegisterProfessorView(View):
	def post(self, request):
		if not HasPerm(request.user):
			return redirect(login_redirect_url)
			
		userForm = UserForm(request.POST)
		profForm = RegisterProfessorForm(request.POST)
		if userForm.is_valid() and profForm.is_valid():
			user = userForm.save(commit=False)
			user.save()
			prof = profForm.save(commit=False)
			prof.user = user
			prof.name = user.first_name + ' ' + user.last_name
			prof.save()
		else:
			return render(request, 'accountsApp/regProfessor.html', { 'user': userForm, 'prof': profForm })
			
		return redirect(home_redirect_url)
	def get(self, request):
		if not HasPerm(request.user):
			return redirect(login_redirect_url)
			
		userForm = UserForm()
		profForm = RegisterProfessorForm()
		return render(request, 'accountsApp/regProfessor.html', { 'user': userForm, 'prof': profForm })