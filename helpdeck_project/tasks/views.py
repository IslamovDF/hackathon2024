from django.shortcuts import render
from django.http import HttpResponse
from .models import Task
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    return render(request, 'tasks\index.html')

def new_task(request):
    if request.method == 'POST':
        new_task_form = Task()
        new_task_form.title = request.POST['title'] if request.POST['title'] else ''
        new_task_form.message = request.POST['message'] if request.POST['message'] else ''
        new_task_form.authors = User.objects.get(id=1)
        new_task_form.closed = False
        new_task_form.save()
        return render(request,
                      'tasks\\success_task.html',
                      {'task_id': new_task_form.id,
                        'message_text': new_task_form.message})
    return render(request, 'tasks\\new_task.html')

def tasks_list(request):
    task_list = Task.objects.all()
    return HttpResponse(', '.join([x.title for x in task_list]))

def detail_task(request, task_id):
    return HttpResponse(f'<h1>Task - {task_id}</h1>')

def about(request):
    return render(request, 'tasks\\about.html')