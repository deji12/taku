from django.contrib import admin
from .models import Assignment, AssignmentMessages

admin.site.register(Assignment)

class MessageAdmin(admin.ModelAdmin):
    list_display = ['assignment', 'sender', 'message']

admin.site.register(AssignmentMessages, MessageAdmin)