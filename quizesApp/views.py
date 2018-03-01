import datetime

from django.conf import settings
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.views import View

from professorsApp.models import Professor
from sessionManagerApp.models import Session
from studentsApp.models import StudentInfo

from .models import Quiz, QuizComplete

login_redirect_url = getattr(settings, 'LOGIN_URL', 'accountsApp:login')
quizes_shown_per_page = getattr(settings, 'NEWS_PER_PAGE', 5)

#TODO Actually use this.
class _quiz: #Should I use this instead of the rubbish down there? xD
    def __init__(student, quiz):
        self.session = quiz.session
        self.quizFile = quiz.quizFile
        self.studentsCompleted = quiz.studentsCompleted
        self.deadline = quiz.deadline
        self.max_grade = quiz.max_grade
        
        if quiz.studentsCompleted.filter(student=student).exists():
            if quiz.studentsCompleted.filter(student=student).first().grade == '---':
                self.status = 'Reviewing Answer'
            else:
                self.status = 'Marked'
        else:
            if quiz.deadline <= timezone.now():
                self.status = 'Ended'
            self.status = 'Not uploaded.'

#TODO Actually implement this.
def HasPerm(user, session):
    # Has permission to delete quizes, view quizes results & change them.
	return True

class QuizesView(View):
    def get(self, request, session_id):
        if not request.user.is_authenticated:
            return redirect(login_redirect_url)

        session = get_object_or_404(Session, id=session_id)

        if session.professor is None:
            return render(request, 'error.html', {})

        prof = None
        if Professor.objects.filter(user=request.user).exists():
            prof = Professor.objects.get(user=request.user)

        if prof is None:
            student = get_object_or_404(StudentInfo, user=request.user)

            if not session in student.sessions.all():
                return render(request, 'error.html', {})
            
            
            quizes_grades = []

            for quiz in session.quiz_set.order_by('-id'):
                if quiz.studentsCompleted.filter(student=student).exists():
                    quizes_grades.append(quiz.studentsCompleted.get(student=student).grade)
                else:
                    if quiz.deadline <= timezone.now():
                        quizes_grades.append('Ended')
                    else:
                        quizes_grades.append('???')

            context = {
                'quizes': session.quiz_set.order_by('-id'),
                'quizes_grades': quizes_grades,
                'session': session,
                'has_perm': HasPerm(request.user, session)
            }
            
            return render(request, 'quizesApp/index.v2.html', context)
        else:
            if session.professor != prof:
                return render(request, 'error.html', {})

            context = {
                'quizes': session.quiz_set.order_by('-id'),
                'session': session,
                'prof': True,
                'has_perm': True,
            }

            context['colors'] = [y <= timezone.now() for y in [x.deadline for x in context['quizes']]]
            return render(request, 'quizesApp/index.v2.html', context)

    #TODO: We need to check 1 file sizes, file extensions.
    def post(self, request, session_id):
        if not request.user.is_authenticated:
            return redirect(login_redirect_url)
        
        session = get_object_or_404(Session, id=session_id)

        #If it's professor posting, it would be a quiz.
        if Professor.objects.filter(user=request.user).exists():
            if session.professor == None:
                return render(request, 'error.html', {})
            if session.professor != Professor.objects.get(user=request.user):
                return render(request, 'error.html', {})
            #TODO Check deadline, Check max_grade
            post_deadline = datetime.datetime.strptime(request.POST.get('date') + " " + request.POST.get('time'), '%Y-%m-%d %H:%M')
            quiz = Quiz(max_grade=request.POST.get('max_grade'), session=session, quizFile=request.FILES['quiz_file'], deadline=post_deadline)
            quiz.save()
            return redirect('quizesApp:view', session_id=session.id)


        student = get_object_or_404(StudentInfo, user=request.user)
        quiz = get_object_or_404(Quiz, id=request.POST.get('quiz_id'))

        # If the student doesn't take this session.
        if not session in student.sessions.all():
            return render(request, 'error.html', {})

        # If the quiz is not in a session the student takes.
        if not quiz in session.quiz_set.all():
            return render(request, 'error.html', {})
        
        # If the student already uploaded an answer.
        if quiz.studentsCompleted.filter(student=student).exists():
            return render(request, 'error.html', {})

        # If quiz already ended.
        if quiz.deadline <= timezone.now():
            return render(request, 'error.html', {})

        answer = QuizComplete(grade="---", answerFile=request.FILES['file'], student=student)
        answer.save()

        quiz.studentsCompleted.add(answer)

        return redirect('quizesApp:view', session_id=session.id)

class DeleteQuizView(View):
    def get(self, request, quiz_id):
        if not request.user.is_authenticated:
            return redirect(login_redirect_url)

        quiz = get_object_or_404(Quiz, id=quiz_id)
        
        if not HasPerm(request.user, quiz.session):
            return render(request, 'error.html', {})

        quiz.delete()

        return redirect('quizesApp:list', kwargs={'session_id': quiz.session.id})

class QuizResultsView(View):
    def get(self, request, quiz_id):
        if not request.user.is_authenticated:
            return redirect(login_redirect_url)

        quiz = get_object_or_404(Quiz, id=quiz_id)

        if not HasPerm(request.user, quiz.session):
            return render(request, 'error.html', {})

        context = {
            'quiz': quiz,
            'answers': quiz.studentsCompleted.all(),
            'grades': range(0, quiz.max_grade+1),
        }

        return render(request, 'quizesApp/quizResults.html', context)

    def post(self, request, quiz_id):
        if not request.user.is_authenticated:
            return redirect(login_redirect_url)

        quiz = get_object_or_404(Quiz, id=quiz_id)

        if not HasPerm(request.user, quiz.session):
            return render(request, 'error.html', {})

        grades = request.POST.getlist('grade')
        i = 0
        for answer in quiz.studentsCompleted.all():
            answer.grade = grades[i]
            i = i + 1
            answer.save()
        
        return redirect('quizesApp:view', session_id=quiz.session.id)
