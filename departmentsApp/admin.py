from django.contrib import admin
from .models import Group, Department

admin.site.register(Department)
admin.site.register(Group)