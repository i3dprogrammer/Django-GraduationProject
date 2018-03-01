from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.conf import settings
from django.utils.dateparse import parse_date, parse_time
from sessionManagerApp.models import Session
from .models import Question, Answer, OnlineExam
from datetime import datetime
from professorsApp.models import Professor
from studentsApp.models import StudentInfo

login_redirect_url = getattr(settings, 'LOGIN_URL', 'accountsApp:login')

class AddNewQuizView(View):
    def get(self, request, session_id):
        return render(request, 'onlineExamsApp/add.html', {'session': Session.objects.get(id=session_id)})
    def post(self, request, session_id):
        try:
            date = parse_date(request.POST.get('date'))
            time = parse_time(request.POST.get('time'))
            duration = int(request.POST.get('duration'))
            grade = int(request.POST.get('grade'))
            exam = OnlineExam.objects.create(session=Session.objects.get(id=session_id), date_time_start = datetime.combine(date, time), duration=duration, quiz_grade=grade)

            params_len = len(request.POST)
            params = (list(request.POST.items()))
            if params_len > 5:
                i = 5
                question = None
                next_answer_correct = False
                while(i < params_len):
                    if params[i][0][0] == 'q':
                        question = Question(exam=exam) # Renew the question
                        question.text = params[i][1]
                        question.save()
                    if params[i][0][0] == 'a':
                        answer = Answer(text=params[i][1], question=question)
                        if next_answer_correct == True:
                            answer.correct = True
                            next_answer_correct = False
                        answer.save()
                    if params[i][0][0] == 'r':
                        next_answer_correct = True
                    i = i + 1
            return redirect('onlineExamsApp:list', session_id=session_id)
        except:
            return redirect('onlineExamsApp:add', session_id=session_id)

class TestView2(View):
    def get(self, request):
        return render(request, 'onlineExamsApp/exam.html', {'session': Session.objects.get(id=40)})

class ListQuizesView(View):
    def get(self, request, session_id):
        if not request.user.is_authenticated:
            return redirect(login_redirect_url)
        
        prof = None

        session = get_object_or_404(Session, id=session_id)

        if Professor.objects.filter(user=request.user).exists():
            if not session.professor == Professor.objects.get(user=request.user):
                return render(request, 'error.html', {})
            prof = True

        if prof is None:
            student = get_object_or_404(StudentInfo, user=request.user)

            if not session in student.sessions.all():
                return render(request, 'error.html', {})

        return render(request, 'onlineExamsApp/index.html', {'session': session, 'prof': prof})

class DeleteQuizView(View):
    def get(self, request, session_id, exam_id):
        if not request.user.is_authenticated:
            return redirect(login_redirect_url)
        
        session = get_object_or_404(Session, id=session_id)

        if Professor.objects.filter(user=request.user).exists() and session.professor == Professor.objects.get(user=request.user):
            exam = OnlineExam.objects.get(id=exam_id)
            exam.delete()
            return redirect('onlineExamsApp:list', session_id = exam.session.id)

        return render(request, 'error.html', {})