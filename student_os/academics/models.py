from django.db import models
from django.conf import settings


class Subject(models.Model):
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    batch = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class FacultySubject(models.Model):
    faculty = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.faculty} - {self.subject}"


class ClassSession(models.Model):
    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE
    )
    faculty = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    room = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.subject} ({self.room})"
