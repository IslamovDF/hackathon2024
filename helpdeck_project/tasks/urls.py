from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("new/", views.new_task, name="new_task"),
    path("new/<str:email>", views.new_task, name="new_task"),
    path('tasks/', views.tasks_list, name='task list'),
    path('dashboard/', views.statistics, name='statistics'),
    path("about/", views.about, name="about"),
    path("task/<int:task_id>/", views.task_info, name="task_info"),
]