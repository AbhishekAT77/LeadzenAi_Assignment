from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm, UpdateTaskForm

# Create your views here.


def index(request):
    todos = Task.objects.all() #To find all the task objects cr
    count_todos = todos.count() #To count total tasks created

    completed_todo = Task.objects.filter(complete=True) # to get completed tasks
    count_completed_todo = completed_todo.count() # to count conpleted tasks

    uncompleted = count_todos - count_completed_todo # to count uncompleted tasks

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = TaskForm()
    context = {
        'todos': todos,
        'form': form,
        'count_todos': count_todos,
        'count_completed_todo': count_completed_todo,
        'uncompleted': uncompleted,
    }
    return render(request, 'todos/index.html', context)

#to update the tasks
def update(request, pk):
    task = Task.objects.get(id=pk)
    if request.method == 'POST':
        form = UpdateTaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = UpdateTaskForm(instance=task)
    context = {
        'form': form
    }
    return render(request, 'todos/update_task.html', context)

#to delete the tasks
def delete(request, pk):
    task = Task.objects.get(id=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('/')
    return render(request, 'todos/delete_task.html')

#to display completed tasks
def completed(request):
    completed_todo = Task.objects.filter(complete=True)
    return render(request, 'todos/completed.html', {"completed":completed_todo})

#to display pending tasks
def pending(request):
    pending_todo = Task.objects.filter(complete=False)
    return render(request, 'todos/completed.html', {"completed":pending_todo})
