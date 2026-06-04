from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm

# Create your views here.

@login_required
def list_and_add_task(request):
    tasks = Task.objects.filter(user = request.user)
    return render(request, 'users/list_task.html', {'tasks': tasks})


@login_required
def list_and_add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('list-task')
    else:
        form = TaskForm()
    task = Task.objects.all()
    return render(request, 'users/add_task.html', {'task': task, 'form': form})
