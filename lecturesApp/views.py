from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.conf import settings
from sessionManagerApp.models import Session
from professorsApp.models import Professor
from studentsApp.models import StudentInfo
from .models import Lecture

login_redirect_url = getattr(settings, 'LOGIN_URL', 'accountsApp:login')

class LecturesView(View):
    def get(self, request, session_id):
        if not request.user.is_authenticated:
            return redirect(login_redirect_url)

        session = get_object_or_404(Session, id=session_id)

        # If there's no professor, there's no quizes/sessions
        if session.professor == None:
            return render(request, 'error.html', {})

        HasPerm = False

        # Check if the professor is the owner of the session.
        if Professor.objects.filter(user=request.user).exists():
            if not session.professor == Professor.objects.get(user=request.user):
                return render(request, 'error.html', {})
            HasPerm = True
        # Check if the student has the session.
        elif StudentInfo.objects.filter(user=request.user).exists():
            if not session in StudentInfo.objects.get(user=request.user).sessions.all():
                return render(request, 'error.html', {})

        context = {
            'session': session,
            'lectures': Lecture.objects.filter(session=session),
            'has_perm': HasPerm,
        }

        return render(request, 'lecturesApp/index.v2.html', context)

    def post(self, request, session_id):
        if not request.user.is_authenticated:
            return redirect(login_redirect_url)

        session = get_object_or_404(Session, id=session_id)

        # If there's no professor, there's no quizes/sessions
        if session.professor == None:
            return render(request, 'error.html', {})

        HasPerm = False

        # Check if the POST made by the owner professor.
        if Professor.objects.filter(user=request.user).exists():
            if not session.professor == Professor.objects.get(user=request.user):
                return render(request, 'error.html', {})
            HasPerm = True
        else:
            return render(request, 'error.html', {})

        lecture = Lecture(session=session, name=request.POST.get('name'), file=request.FILES['file'])
        lecture.save()

        context = {
            'session': session,
            'lectures': Lecture.objects.filter(session=session),
            'has_perm': HasPerm,
        }

        return render(request, 'lecturesApp/index.v2.html', context)

class DeleteLectureView(View):
    def get(self, request, lecture_id):
        if not request.user.is_authenticated:
            return redirect(login_redirect_url)

        lecture = get_object_or_404(Lecture, id=lecture_id)

        session = lecture.session

        # If there's no professor, there's no quizes/sessions
        if session.professor == None:
            return render(request, 'error.html', {})

        HasPerm = False

        # Check if the POST made by the owner professor.
        if Professor.objects.filter(user=request.user).exists():
            if not session.professor == Professor.objects.get(user=request.user):
                return render(request, 'error.html', {})
            HasPerm = True
        else:
            return render(request, 'error.html', {})

        lecture.delete()

        return redirect('lecturesApp:view', session_id=session.id)
