from django.contrib import admin
from .models import PublicNotification, UserSemester, CompletedCourse

admin.site.register(PublicNotification)
admin.site.register(UserSemester)
admin.site.register(CompletedCourse)