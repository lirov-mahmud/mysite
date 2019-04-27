from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('todo/<int:pk>/', views.detail, name='detail'),
	path('todo/new/', views.new, name='new'),
	path('todo/<int:pk>/edit>', views.edit, name='edit'),
]