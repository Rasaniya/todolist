from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.

def index(request):
    form = TaskForm()

    tasks = Task.objects.all()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    context = {'tasks': tasks, 'form': form}
    return render(request, 'todo/list.html', context)
    
def update_task(request, pk):
    tasks = Task.objects.get(id=pk)

    form = TaskForm(instance=tasks)

    context = {'form':form}

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=tasks)
        if form.is_valid():
            form.save()
        return redirect('/')

    return render(request, 'todo/update_task.html', context)

def delete_task(request, pk):
    item = Task.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
    
        return redirect('/')

    context = {'item':item}
    return render(request, 'todo/delete.html', context)