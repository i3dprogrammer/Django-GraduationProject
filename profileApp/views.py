from django.conf import settings
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.views import View

from professorsApp.models import Professor
from sessionManagerApp.models import Session
from studentsApp.models import StudentInfo

from .models import PublicNotification

login_redirect_url = getattr(settings, 'LOGIN_URL', 'accountsApp:login')


class daySessions:
    def __init__(self, sessions, day):
        self.sessions = sessions
        self.day = day
    sessions = None
    day = None


class ProfileHomeView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect(login_redirect_url)

        prof = None
        student = None

		# Could also use StudentInfo to check.
        if Professor.objects.filter(user=request.user).exists():
            prof = Professor.objects.get(user=request.user)
            notifications = PublicNotification.objects.filter(showToProfessors=True)
        else:
            student = StudentInfo.objects.get(user=request.user)
            notifications = PublicNotification.objects.filter(showToStudents=True)

        context = {
            'notifications': notifications,
            'professor': prof,
            'student': student,
        }
        return render(request, 'profileApp/home.html', context)


class ScheduleView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect(login_redirect_url)

        prof = None
        student = None

		# Could also use StudentInfo to check.
        if Professor.objects.filter(user=request.user).exists():
            prof = Professor.objects.get(user=request.user)
            notifications = PublicNotification.objects.filter(showToProfessors=True)
        else:
            student = StudentInfo.objects.get(user=request.user)
            notifications = PublicNotification.objects.filter(showToStudents=True)

        context = {
			'professor': prof,
			'sessions': [],
			'notifications': notifications,
		}
        
        if prof:
            for day in Session.DAYS_OF_WEEK_CHOICES:
                context['sessions'].append(daySessions(prof.session_set.filter(dayOfWeek=day[0]).order_by('startTime'), day[1]))
        else:
            for day in Session.DAYS_OF_WEEK_CHOICES:
                context['sessions'].append(daySessions(student.sessions.filter(dayOfWeek=day[0]).order_by('startTime'), day[1]))

        context['maxLectures'] = range(
            max([len(x.sessions) for x in context['sessions']]))

        return render(request, 'profileApp/schedule.html', context)


class OldSemestersView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect(login_redirect_url)

        student = get_object_or_404(StudentInfo, user=request.user)

        context = {
            'notifications': PublicNotification.objects.filter(showToStudents=True),
            'semesters': student.usersemester_set.all(),
        }
        return render(request, 'profileApp/semesters.html', context)

class SessionsView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect(login_redirect_url)

        prof = None
        student = None

		# Could also use StudentInfo to check.
        if Professor.objects.filter(user=request.user).exists():
            prof = Professor.objects.get(user=request.user)
            notifications = PublicNotification.objects.filter(showToProfessors=True)
        else:
            student = StudentInfo.objects.get(user=request.user)
            notifications = PublicNotification.objects.filter(showToStudents=True)

        context = {
            'notifications': notifications,
            'professor': prof,
            'student': student,
        }
        return render(request, 'profileApp/current_sessions.html', context)