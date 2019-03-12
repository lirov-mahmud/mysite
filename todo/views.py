
from django.shortcuts import render
from .models import *


def index(request):
	todolist = TodoList.objects.all()
	context = {'todolist' : todolist}
	return render(request, 'todo/index.html', context)