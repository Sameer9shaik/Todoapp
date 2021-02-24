from django.contrib import admin
from todoapp.models import*

# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = ['Title','Time','Task_type']
    list_display_links = ['Title','Time','Task_type']

admin.site.register(Task,TaskAdmin)






