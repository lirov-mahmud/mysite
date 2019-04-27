from django.db import models
from django import forms
from django.conf import settings


class TodoList(models.Model):
    item = models.CharField(max_length=100)

    Active = 'avtive'
    Done = 'done'
    Canceled = 'canceled'

    Status = ((Active, 'avtive'),(Done, 'done'),(Canceled, 'canceled'),)

    status = models.CharField(max_length=15, choices=Status, default=Active)

    def __str__(self):
    	return self.item