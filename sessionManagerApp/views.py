from datetime import date, datetime, timedelta

from django.conf import settings
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View

from coursesApp.models import Course
from departmentsApp.models import Department, Group
from professorsApp.models import Professor
from settingsApp.models import Setting
from studentsApp.models import StudentInfo

from .models import Session

login_redirect_url = getattr(settings, 'LOGIN_URL', 'accountsApp:login')
view_sessions_redirect_url = 'sessionManagerApp:viewSessions'

# SHOULD PROBABLY MAKE THE THREE FUNCTIONS INTO ONE, TO AVOID LOTS OF DB USAGE,
# OR WE SHOULD CACHE THE QUERUES GLOBALLY.

def SessionSameGroup(s, u):
	return s.course.group == get_object_or_404(StudentInfo, user=u).group

def PrerequistiesDone(s, u):
	c_list = []
	for semester in StudentInfo.objects.get(user=u).usersemester_set.all():
		for c_c in semester.completedcourse_set.all():
			c_list.append(c_c.course)
	return set(s.course.prequels.all()).issubset(c_list)
	
def SessionCompleted(s, u):
	for semester in StudentInfo.objects.get(user=u).usersemester_set.all():	
		for c_course in semester.completedcourse_set.all():
			if s.course == c_course.course:
				return True
	return False
	
def SessionOnGoing(s, u):
	if s in StudentInfo.objects.get(user=u).sessions.all():
		return True
	return False
	
def DoDataForEveryUser():
	for u in User.objects.all():
		us = UserInfo(user=u)
		us.save()

class ManageSessionsView(View):
	def post(self, request):
		if not request.user.is_authenticated:
			return redirect(login_redirect_url)
		if not Setting.objects.first().canChangeSessions:
			return render(request, 'sessionManagerApp/error.html', {})
		
		group = request.POST.get("selectedDepartment")

		if group:
			info = StudentInfo.objects.get(user=request.user)
			info.group = get_object_or_404(Group, name=group)
			info.save()
			return redirect('sessionManagerApp:manage')

		selectedSessions = [Session.objects.get(id=x) for x in request.POST.getlist("selectedCourses")]
		errorList = []
		
		# Check if there's any confliction between courses timings.
		conflictError = False
		course1Conflict = ""
		course2Conflict = ""
		for x in selectedSessions:
			if conflictError:
				break
				
			for y in selectedSessions:
				if x != y and y.startTime >= x.startTime and y.startTime < x.endTime and x.dayOfWeek == y.dayOfWeek:
					conflictError = True
					course1Conflict = x.course.name
					course2Conflict = y.course.name
					break
		
		# Check if there's any errors with hours / week 
		selectedHours = sum([x.course.duration.hour for x in selectedSessions])
		minHours = Setting.objects.all()[0].minHoursWeek
		maxHours = Setting.objects.all()[0].maxHoursWeek
		hoursError =  selectedHours < minHours or selectedHours > maxHours
		
		# Check for duplicate courses
		duplicateError = False
		duplicateName = ""
		coursesList = {}
		for session in selectedSessions:
			if session.course.name in coursesList:
				duplicateError = True
				duplicateName = session.course.name
				break
			else:
				coursesList[session.course.name] = 1

		# Add errors
		if conflictError:
			errorList.append(("There's confliction between the courses you choosen ({0} - {1}). Consider choosing different course times.").format(course1Conflict, course2Conflict))
		if hoursError:
			errorList.append(("You cannot save because your weekly hours doesn't meet the requirements: Minimum hours/week = {0}, Maximmum hours/week = {1}.").format(minHours, maxHours))
		if duplicateError:
			errorList.append(("There's duplicate courses you've selected with different locations/times ({0}), you're only allowed to register a course once.").format(duplicateName))
		if len([s for s in selectedSessions if not PrerequistiesDone(s, request.user)]) > 0:
			errorList.append("You shouldn't be seeing this! It appears like you've selected some courses without completing their prerequisties.")
		if len([s for s in selectedSessions if SessionCompleted(s, request.user)]) > 0:
			errorList.append("You shouldn't be seeing this! It appears you've selected a completed course already.")

		# Show errors, if any.
		if len(errorList) > 0:
			context = {
				'allSessions': [x for x in Session.objects.all() if not SessionCompleted(x, request.user) and PrerequistiesDone(x, request.user) and x not in selectedSessions],
				'userSessions': selectedSessions,
				'allCourses': Course.objects.all(),
				'userTotalHours': selectedHours,
				'minHoursWeek': Setting.objects.all()[0].minHoursWeek,
				'maxHoursWeek': Setting.objects.all()[0].maxHoursWeek,
				'errorList': errorList,
			}
			
			return render(request, 'sessionManagerApp/manage.html', context)
		else:
			userObj = StudentInfo.objects.get(user=request.user)
			userObj.sessions.clear()
			
			for session in selectedSessions:
				userObj.sessions.add(session)
				
			return redirect('profileApp:profile')
		
	def get(self, request):
		if not request.user.is_authenticated:
			return redirect(login_redirect_url)
		if not Setting.objects.first().canChangeSessions:
			return render(request, 'sessionManagerApp/error.html', {})
		if not StudentInfo.objects.filter(user=request.user).exists():
			return render(request, 'sessionManagerApp/error.html', {})

		u = request.user

		info = get_object_or_404(StudentInfo, user=u)
		if Department.objects.filter(prequel=info.group, year=info.year).exists():
			context = {
				'curr_group': info.group,
				'allowed_groups': Department.objects.get(prequel=info.group, year=info.year).sequels.all(),
			}
			return render(request, 'sessionManagerApp/manage.html', context )

		sessions = StudentInfo.objects.get(user=request.user).sessions.all()
		context = {
			'allSessions': [x for x in Session.objects.all() if not SessionOnGoing(x, u) and not SessionCompleted(x, u) and PrerequistiesDone(x, u) and SessionSameGroup(x, u)],
			'userSessions': sessions,
			'allCourses': Course.objects.all(),
			'userTotalHours': sum([x.course.duration.hour for x in sessions]),
			'minHoursWeek': Setting.objects.all()[0].minHoursWeek,
			'maxHoursWeek': Setting.objects.all()[0].maxHoursWeek,
		}
		
		return render(request, 'sessionManagerApp/manage.html', context )
		
class ViewSessionsView(View):
	def get(self, request, session_id):
		if not request.user.is_authenticated:
			return redirect(login_redirect_url)
			
		session = get_object_or_404(Session, id=session_id)
		
		if not Professor.objects.filter(user=request.user).exists():
			return render(request, 'sessionManagerApp/error.html', {})

		if Professor.objects.get(user=request.user) != session.professor:
			return render(request, 'sessionManagerApp/error.html', {})

		return render(request, 'sessionManagerApp/view.html', {'session': session } )
