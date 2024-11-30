from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm


# Create your models here.
class TypeTask(models.Model):
    type = models.CharField(max_length=50)

    def __str__(self):
        return self.type

class Task(models.Model):
    title = models.CharField(max_length=1024)
    message = models.TextField()
    authors = models.CharField(max_length=1024)
    contractor = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    created = models.DateTimeField("date published", auto_now_add= True)
    closed = models.BooleanField(default=False)
    typetask = models.ForeignKey(TypeTask, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

class Info(models.Model):
    autor_ID = models.CharField(max_length=50)
    address = models.CharField(max_length=1024)
    priority = models.IntegerField(default=0)
    email = models.CharField(max_length=1024)

    def __str__(self):
        return self.email



class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'message', 'authors']