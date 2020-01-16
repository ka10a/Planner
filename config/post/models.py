from django.db import models
from django.urls import reverse


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    @property
    def get_html_url(self):
        url = reverse('event_edit', args=(self.id,))
        return f'<a href="{url}"> {self.title} </a>'

    def __str__(self):
        return self.name


class ToDoItem(models.Model):
    name = models.CharField(max_length=200)
    due_date = models.DateField('task date')
    category = models.CharField(max_length=100)
    done = models.BooleanField(default=False)
    user = models.BigIntegerField(default=0)

    def __str__(self):
        return self.name
