from django.shortcuts import render
from django.views import View
from sessionManagerApp.models import Session

class TestView(View):
    def get(self, request):
        return render(request, 'onlineExamsApp/add.html', {'session': Session.objects.get(id=40)})
    def post(self, request):
        print(request.body)
        return render(request, 'onlineExamsApp/add.html', {'session': Session.objects.get(id=40)})

class TestView2(View):
    def get(self, request):
        return render(request, 'onlineExamsApp/exam.html', {'session': Session.objects.get(id=40)})