from django.shortcuts import render
from django.http import HttpResponse
from .models import Task
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    return render(request, 'tasks\index.html')

def new_task(request, email=None):
    if request.method == 'POST':
        new_task_form = Task()
        new_task_form.title = request.POST['title'] if request.POST['title'] else ''
        new_task_form.message = request.POST['message'] if request.POST['message'] else ''
        new_task_form.authors = request.POST['authors_email'] if request.POST['authors_email'] else ''
        new_task_form.closed = False
        new_task_form.save()
        return render(request,
                      'tasks/success_task.html',
                      {'task_id': new_task_form.id,
                        'message_text': new_task_form.message})
    return render(request, 'tasks/new_task.html', {'mail': email if email else ''})

def tasks_list(request):
    tasks_list_to_page = Task.objects.all()
    print(len(tasks_list_to_page))
    # return HttpResponse(', '.join([x.title for x in tasks_list_to_page]))
    return render(request, 'tasks/task_list.html', {'task_list': tasks_list_to_page})

def detail_task(request, task_id):
    return HttpResponse(f'<h1>Task - {task_id}</h1>')

def statistics(request):
    return render(request, 'tasks/statistics.html',
                  {'task_count': len(Task.objects.all()),
                   'user_count': len(User.objects.all())})

def about(request):
    return render(request, 'tasks/about.html')