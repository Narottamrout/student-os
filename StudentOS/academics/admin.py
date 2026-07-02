from django.contrib import admin
from .models import Subject, FacultySubject, ClassSession

admin.site.register(Subject)
admin.site.register(FacultySubject)
admin.site.register(ClassSession)