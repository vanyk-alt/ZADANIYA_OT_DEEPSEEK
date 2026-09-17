from django.urls import path
from  . import views

urlpatterns =[
    path('',views.task_list, name='task_list'),
    path('task/<int:task_id>/toggle/',views.toggle_task, name='toggle_task'),
    path('task/<int:task_id>delete/',views.delete_task_confirm, name='delete_task_confirm'),
    path('task/<int:task_id>/delete/confirm', views.delete_task, name='delete_task'),
]