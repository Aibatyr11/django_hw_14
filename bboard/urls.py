from django.urls import path

from bboard.views import *

urlpatterns = [
    path('', index),

    path('html/', index_html, name='index_html'),

    path('<int:rubric_id>/', by_rubric, name='by_rubric'),

    path('add/', BbCreateView.as_view(), name='add'),

    path('crypto/<slug:slug>/', get_by_slug, name="get_by_slug"),

    path('comment/<slug:slug>/', comment, name="comment"),

    path('comment_delete/<slug:slug>/', comment_delete, name="comment_delete"),

    #hw
    # Главная страница со списком задач
    path('tasks/', views.task_list, name='task_list'),

    # Просмотр задачи по ID
    path('tasks/<int:task_id>/', views.view_task, name='view_task'),

    # Добавление новой задачи
    path('tasks/add/', views.TaskCreateView.as_view(), name='add_task'),

    # Редактирование задачи по ID
    path('tasks/edit/<int:task_id>/', views.edit_task, name='edit_task'),

    # Удаление задачи по ID
    path('tasks/delete/<int:task_id>/', views.delete_task, name='delete_task'),

    # Поиск задач
    path('tasks/search/', views.search_tasks, name='search_tasks'),

    # Задачи по статусу (выполненные/невыполненные)
    path('tasks/status/<slug:status>/', views.tasks_by_status, name='tasks_by_status'),





]
