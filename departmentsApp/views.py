from django.conf import settings
from django.shortcuts import redirect, render, reverse, get_object_or_404
from django.views import View
from django.http import HttpResponse

from .models import Group, Department
from studentsApp.models import StudentInfo
from coursesApp.models import Course
from settingsApp.models import Setting

login_redirect_url = getattr(settings, 'LOGIN_URL', 'accountsApp:login')

def getList(dep):
    seqList = []
    for group in dep.sequels.all():        
        if Department.objects.filter(prequel=group).exists():
            seqList.append("<a href='{0}'>{1}</a>".format(reverse('departmentsApp:view_department', kwargs={'group_id':group.id}), group.name))
            seqList.append(getList(Department.objects.get(prequel=group)))
        else:
            seqList.append("<a href='{0}'>{1}</a>".format(reverse('departmentsApp:view_department', kwargs={'group_id':group.id}), group.name))

    return seqList


class DepartmentsView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect(login_redirect_url)
        
        context = {
            'var': ['None', getList(Department.objects.get(prequel__name='None'))],
        }

        return render(request, 'departmentsApp/departments.html', context)

class DepartmentView(View):
    def get(self, request, group_id):
        if not request.user.is_authenticated:
            return redirect(login_redirect_url)

        dep = None
        if Department.objects.filter(prequel__id=group_id).exists():
            dep = Department.objects.get(prequel__id=group_id)

        context = {
            'group': get_object_or_404(Group, id=group_id),
            'show_mark': StudentInfo.objects.get(user=request.user).group.id == int(group_id),
            'dep': dep,
            'group_courses': Course.objects.filter(group__id=group_id),
            'c_list': StudentInfo.objects.filter(user=request.user).values_list('usersemester__completedcourse__course__name', flat=True)
        }
        return render(request, 'departmentsApp/view_department.html', context)