from django.db import models


class Event(models.Model):
    date = models.DateTimeField('event date')
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Calendar(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class ToDoItem(models.Model):
    name = models.CharField(max_length=200)
    todo = models.CharField(max_length=1000)
    date = models.DateField('task date')
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.name
