from django.contrib import admin
from .models import Log, LogbookEntry

admin.site.register(Log)
admin.site.register(LogbookEntry)
