from django.shortcuts import render,redirect
from .models import Task

def task_list(request):
    if request.method == "POST":
        title = request.POST.get('title')
        if title:
            Task.objects.create(title=title)
            return redirect('task_list')
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

def toggle_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.done = not task.done
    task.save()
    return redirect('task_list')