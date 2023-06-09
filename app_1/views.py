from django.shortcuts import render, redirect
from .models import Task
from.forms import TasksForm

# Create your views here.

def index(request):
    task = Task.objects.all()
    if request.method =='POST':
        name = request.POST.get('task_name')
        prior = request.POST.get('priority')
        task_date = request.POST.get('task_date')
        tas = Task(task_name=name, priority=prior, task_date=task_date)
        tas.save()
    context = {'task':task}
    return render(request, 'index.html', context)


def delete(request, id):
    task = Task.objects.get(id = id)
    if request.method == 'POST':
        task.delete()
        return redirect('/')
    return render(request, 'delete.html')

def update(request, id):
    task = Task.objects.get(id=id)
    form = TasksForm(request.POST or None,instance=task)
    print('Form Is:', form)
    if form.is_valid():
        form.save()
        return redirect('/')
    context ={'form':form, 'task':task}
    return render(request, 'update.html', context)