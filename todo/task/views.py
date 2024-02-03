from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import render , redirect
from .models import * 
from .forms import * 
from django.contrib import messages


# Create your views here.
def index(request):
    if request.method =="POST":
        task_form = TaskForm(request.POST)
        if task_form.is_valid():
            task_form.save()
            messages.success(request, ('Your movie was successfully added!'))
        else:
            messages.error(request, 'Error saving form')
        return redirect("/")
    task_form = TaskForm()
    tasks = Task.objects.all()
    return render(request=request,template_name="task/list.html",context={'tasks_form':task_form, 'tasks':tasks})


def update_task(request,pk):
    task = Task.objects.get(id=pk)
    task_form = TaskForm(instance=task)
    if request.method =='POST':
        task_form = TaskForm(request.POST,instance=task)
        if task_form.is_valid():
            task_form.save()
            return redirect("/")
    context={'task_form':task_form}    
    return render(request,'task/update_task.html',context)


def delete(request,pk):
    item = Task.objects.get(id=pk)
    if request.method =='POST':
        item.delete()
        return redirect("/")
    context={'item':item}    
    return render(request,'task/delete.html',context)