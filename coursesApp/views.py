from django.conf import settings
from django.shortcuts import redirect, render, get_object_or_404
from django.views import View

from departmentsApp.models import Department, Group
from studentsApp.models import StudentInfo

from .models import Course

login_redirect_url = getattr(settings, 'LOGIN_URL', 'accountsApp:login')

class CoursesGroup:
    def __init__(self, group, courses):
        self.group = group
        self.courses = courses

class CoursesViewVersion2(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect(login_redirect_url)

        student_info_query = StudentInfo.objects.filter(user=request.user)

        c_list = student_info_query.values_list('usersemester__completedcourse__course__name', flat=True)
        d_list = [x.name for x in Course.objects.all() if not set(x.prequels.values_list('name', flat=True)).issubset(c_list) or student_info_query.first().group!=x.group]
        
        context = {
            'courses_groups': [CoursesGroup(x, Course.objects.filter(group=x)) for x in Group.objects.all()],
            'user_completed_courses': c_list,
            'denied_courses': d_list,
        }

        return render(request, 'coursesApp/courses_groups.html', context)

class CourseView(View):
    def get(self, request, course_id):
        if not request.user.is_authenticated:
            return redirect(login_redirect_url)

        c_list = StudentInfo.objects.filter(user=request.user).values_list('usersemester__completedcourse__course__name', flat=True)

        context = {
            'course': get_object_or_404(Course, id=course_id),
            'completed': get_object_or_404(Course, id=course_id).name in c_list,
        }
        return render(request, 'coursesApp/view_course.html', context)