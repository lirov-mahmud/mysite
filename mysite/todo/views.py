from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import ListForm


def index(request):
	todo = TodoList.objects.all()
	return render(request, 'todo/index.html', {'todo': todo})


def new(request):
	if request.method == "POST":
		form = ListForm(request.POST)
		if form.is_valid():
			todo = form.save(commit=False)
			todo.save()
			return redirect('detail', pk=todo.pk)
	else:
		form = ListForm()
	return render(request, 'todo/EditTodo.html', {'form': form})

def detail(request, pk):
	todo = get_object_or_404(TodoList, pk=pk)
	return render(request, 'todo/detail.html', {'todo': todo })


def edit(request, pk):
	todo = get_object_or_404(TodoList, pk=pk)
	if request.method == "POST":
		form = ListForm(request.POST, instance=todo)
		if form.is_valid():
			todo = form.save(commit=False)
			todo.save()
			return redirect('detail', pk=todo.pk)
	else:
		form = ListForm(instance=todo)
	return render(request, 'todo/EditTodo.html', {'form': form})