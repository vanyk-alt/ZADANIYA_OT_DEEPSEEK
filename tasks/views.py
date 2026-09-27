from django.shortcuts import render,redirect
from .models import Task

def task_list(request):
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description', '')

        if title:
            Task.objects.create(title=title, description=description)
            return redirect('task_list')
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

def toggle_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.done = not task.done
    task.save()
    return redirect('task_list')

def delete_task_confirm(request, task_id):
    task =  Task.objects.get(id=task_id)
    return render(request, 'tasks/delete_confrim.html', {'task': task})

def delete_task(request, task_id):
    if request.method == "POST":
        task = Task.objects.get(id=task_id)
        task.delete()
    return redirect(task_list)

def task_detail(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == "POST":
        description= request.POST.get('description')
        if description:
            task.description = description
            task.save()
        return redirect('task_detail',task_id=task.id)
    return render(request, 'tasks/task_detail.html', {'task': task})
