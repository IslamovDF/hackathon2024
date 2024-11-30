from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("new/", views.new_task, name="new_task"),
    path('tasks/', views.tasks_list, name='list'),
    path('dashboard/', views.statistics, name='statistics'),
    path("about/", views.about, name="about"),
    path("<int:task_id>/", views.detail_task, name="detail_task"),
]