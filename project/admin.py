from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(staff)
admin.site.register(realtime)
admin.site.register(project)
admin.site.register(projectasset)
admin.site.register(projectres)
admin.site.register(task)
admin.site.register(activity_log)
admin.site.register(task_deliverables)
