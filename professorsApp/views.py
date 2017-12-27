from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.conf import settings
from .models import Professor
from sessionManagerApp.models import Course
from .forms import AddProfessorForm, AddCourseForm
# Create your views here.

login_redirect_url = getattr(settings, 'LOGIN_URL', 'accountsApp:login')
professors_per_page = getattr(settings, 'PROFESSORS_PER_PAGE', 5)
courses_per_page = getattr(settings, 'COURSES_PER_PAGE', 10)

club_name = "ProfessorsManagerClub"
def HasPerm(user):
	return user.groups.filter(name=club_name).exists()

class ProfessorListView(View):
	def get(self, request, page_num='1'):
		start = ((int(page_num) - 1) * professors_per_page)
		next_page = ''
		prev_page = ''
		if Professor.objects.all().count() > (start + professors_per_page):
			next_page = int(page_num) + 1
		if int(page_num) > 1:
			prev_page = int(page_num) - 1
		context = {
			'latest': Professor.objects.order_by('-id')[start:(professors_per_page+start)],
			'next_page': next_page,
			'prev_page': prev_page,
			'has_perm':HasPerm(request.user)
		}
		return render(request, 'professorsApp/professors.html', context)

class CourseListView(View):
	def get(self, request, page_num='1'):
		start = ((int(page_num) - 1) * courses_per_page)
		next_page = ''
		prev_page = ''
		if Course.objects.all().count() > (start + courses_per_page):
			next_page = int(page_num) + 1
		if int(page_num) > 1:
			prev_page = int(page_num) - 1
		context = {
			'latest': Course.objects.order_by('-id')[start:(courses_per_page+start)],
			'next_page': next_page,
			'prev_page': prev_page,
			'has_perm':HasPerm(request.user)
		}
		
		return render(request, 'professorsApp/courses.html', context)
		
class ProfessorView(View):
	def get(self, request, prof_id):
		return render(request, 'professorsApp/viewProfessor.html', { 'professor': get_object_or_404(Professor, id=prof_id)})
		
class CourseView(View):
	def get(self, request, course_id):
		return render(request, 'professorsApp/viewCourse.html', { 'course': get_object_or_404(Course, id=course_id), 'has_perm':HasPerm(request.user) })
		

class AddProfessorView(View):
	def post(self, request):
		if not HasPerm(request.user):
			return redirect(login_redirect_url)
			
		form = AddProfessorForm(request.POST)
		if form.is_valid():
			form.save()
		else:
			return render(request, 'professorsApp/addProfessor.html', {'form':form})	
		return redirect('professorsApp:home')
		
	def get(self, request):
		if not HasPerm(request.user):
			return redirect(login_redirect_url)
			
		form = AddProfessorForm()
		return render(request, 'professorsApp/addProfessor.html', {'form':form})
		
class EditProfessorView(View):
	def post(self, request, prof_id):
		if not HasPerm(request.user):
			return redirect(login_redirect_url)
			
		form = AddProfessorForm(request.POST, instance=get_object_or_404(Professor, id=prof_id))
		if form.is_valid():
			form.save()
		else:
			return render(request, 'professorsApp/editProfessor.html', { 'form':form })
		return redirect('professorsApp:home')
		
	def get(self, request, prof_id):
		if not HasPerm(request.user):
			return redirect(login_redirect_url)
		form = AddProfessorForm(instance=get_object_or_404(Professor, id=prof_id))
		return render(request, 'professorsApp/editProfessor.html', { 'form':form })
		
class DeleteProfessorView(View):
	def get(self, request, prof_id):
		if not HasPerm(request.user):
			return redirect(login_redirect_url)
		get_object_or_404(Professor, id=prof_id).delete()
		return redirect('professorsApp:home')
		
class AddCourseView(View):
	def post(self, request):
		if not HasPerm(request.user):
			return redirect(login_redirect_url)
		
		print(request.POST.getlist('prequels'))
		form = AddCourseForm(request.POST)
		if form.is_valid():
			form.save()
		else:
			return render(request, 'professorsApp/addCourse.html', {'form':form})
		return redirect('professorsApp:coursePage', page_num=1)
		
	def get(self, request):
		if not HasPerm(request.user):
			return redirect(login_redirect_url)
			
		form = AddCourseForm()
		return render(request, 'professorsApp/addCourse.html', {'form':form})
		
class EditCourseView(View):
	def post(self, request, course_id):
		if not HasPerm(request.user):
			return redirect(login_redirect_url)
			
		form = AddCourseForm(request.POST, instance=get_object_or_404(Course, id=course_id))
		if form.is_valid():
			form.save()
		else:
			return render(request, 'professorsApp/editCourse.html', {'form':form })
		return redirect('professorsApp:coursePage', page_num=1)
		
	def get(self, request, course_id):
		if not HasPerm(request.user):
			return redirect(login_redirect_url)
		form = AddCourseForm(instance=get_object_or_404(Course, id=course_id))
		return render(request, 'professorsApp/editCourse.html', {'form':form })
		
class DeleteCourseView(View):
	def get(self, request, course_id):
		if not HasPerm(request.user):
			return redirect(login_redirect_url)
		get_object_or_404(Course, id=course_id).delete()
		return redirect('professorsApp:coursePage', page_num=1)