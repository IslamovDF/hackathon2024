from django.shortcuts import render
from django.http import HttpResponse
from .models import Task
from .models import TypeTask
from .models import Priority
from django.contrib.auth.models import User

# Create your views here.
def yandex_gpt(text_for_user):
    import requests
    prompt = {
    "modelUri": "gpt://b1gkb4guem02kb4oa39o/yandexgpt-lite",
    "completionOptions": {
        "stream": False,
        "temperature": 0.6,
        "maxTokens": "2000"
    },
    "messages": [
        {
            "role": "system",
            "text": "Ты ассистент секретаря, который принимает заявки в службе компьютерной технической поддержки."
        },
        {
            "role": "user",
            "text": "Привет, Секретарь! Прочитай обращение пользователя и определи к какой категории из трех указанных (1.обслуживание (обновления, техподдержка и т.д.), 2.инциденты (неполадки системы или оборудования критически препятствующие работе), 3. запросы на изменение состояния (установка нового оборудования или ПО)) ты бы отнес следующее обращение. Ответь одной цифрой - порядковым номером категории"
        },
        {
            "role": "assistant",
            "text": "Привет! Чтобы обрабатывать тексты, тебе нужно знать русский язык и природу человека. Начнем с изучения основных обращений в тех.поддержку."
        },
        {
            "role": "user",
            "text": text_for_user
        }
                ]
    }
    url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
    headers = {
    "Content-Type": "application/json",
    "Authorization": "Api-Key AQVNxBeG9c3sQp7qXi5qUSrTAArNxxKypW8gOCov"
    }
    response = requests.post(url, headers=headers, json=prompt)
    result = response.text
    return ''.join(filter(str.isdigit, result))[0]


def index(request):
    return render(request, 'tasks\index.html')

def task_info(request, task_id):
    task = Task.objects.get(id=task_id)
    return render(request, 'tasks/task_info.html', {'task': task})

def new_task(request, email=None):
    if request.method == 'POST':
        new_task_form = Task()
        id_type_task = yandex_gpt(request.POST['message'])
        print(id_type_task)
        new_task_form.title = request.POST['title'] if request.POST['title'] else ''
        new_task_form.message = request.POST['message'] if request.POST['message'] else ''
        new_task_form.authors = request.POST['authors_email'] if request.POST['authors_email'] else ''
        new_task_form.contractor = User.objects.get(id=1)
        new_task_form.typetask = TypeTask.objects.get(id=id_type_task)
        new_task_form.closed = False
        new_task_form.save()
        return render(request,
                      'tasks/success_task.html',
                      {'task_id': new_task_form.id,
                        'message_text': new_task_form.message})
    return render(request, 'tasks/new_task.html', {'mail': email if email else ''})

def tasks_list(request):
    tasks_list_to_page = Task.objects.all()
    prior = [p.level for p in Priority.objects.all()]
    print(prior)
    print(type(prior))
    # print(len(tasks_list_to_page[0].))
    # return HttpResponse(', '.join([x.title for x in tasks_list_to_page]))
    return render(request, 'tasks/task_list.html', {'task_list': tasks_list_to_page,
                                                    'prior': prior})

def detail_task(request, task_id):
    return HttpResponse(f'<h1>Task - {task_id}</h1>')

def statistics(request):
    return render(request, 'tasks/statistics.html',
                  {'task_count': len(Task.objects.all()),
                   'user_count': len(User.objects.all())})

def about(request):
    return render(request, 'tasks/about.html')