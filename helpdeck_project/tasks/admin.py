from django.contrib import admin
from .models import Task
from .models import Info
from .models import TypeTask

admin.site.register(Task)
admin.site.register(Info)
admin.site.register(TypeTask)
# Register your models here.
