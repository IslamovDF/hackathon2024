from django.contrib import admin
from .models import Task
from .models import Info
from .models import TypeTask
from .models import Priority

admin.site.register(Task)
admin.site.register(Info)
admin.site.register(TypeTask)
admin.site.register(Priority)
# Register your models here.
