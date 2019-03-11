from django.shortcuts import render
from django.http import HttpResponse

def(request):
	context = {}
	return render(request, 'todo/index.html', context)