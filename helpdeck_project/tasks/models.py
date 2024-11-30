from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=1024)
    message = models.TextField()
    authors = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField("date published", auto_now_add= True)
    closed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'message', 'authors']