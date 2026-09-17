from django.urls import path
from  . import views

urlpatterns =[
    path('',views.task_list, name='task_list'),
    path('task/<int:task_id>/toggle/',views.toggle_task, name='toggle_task'),
]