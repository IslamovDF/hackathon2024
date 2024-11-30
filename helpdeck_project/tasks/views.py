from django.shortcuts import render
from django.http import HttpResponse
from .models import Task

# Create your views here.

def index(request):
    return render(request, 'tasks\index.html')

def new_task(request):
    if request.method == 'POST':
        return HttpResponse(request.POST['title'])
    return render(request, 'tasks\\new_task.html')

def tasks_list(request):
    task_list = Task.objects.all()
    return HttpResponse(', '.join([x.title for x in task_list]))

def detail_task(request, task_id):
    return HttpResponse(f'<h1>Task - {task_id}</h1>')

def about(request):
    return render(request, 'tasks\\about.html')