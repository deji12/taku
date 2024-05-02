from django.db import models
from django.conf import settings
    
class Log(models.Model):
    date_created = models.DateField()
    details = models.TextField()
    
    def __str__(self):
        return self.details


class LogbookEntry(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateField()
    activity = models.CharField(max_length=200)
    assessment = models.CharField(max_length=200, blank=True)
    mark = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f'{self.student.username} - {self.date}'