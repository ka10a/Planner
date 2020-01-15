from django.db import models


class Event(models.Model):
    date = models.DateTimeField('event date', null=False,
                            help_text="This field is required")
    name = models.CharField(max_length=200, null=False,
                            help_text="This field is required")

    def __str__(self):
        return self.name


class Calendar(models.Model):
    name = models.CharField(max_length=200, null=False,
                            help_text="This field is required")

    def __str__(self):
        return self.name


class ToDoItem(models.Model):
    name = models.CharField(max_length=200)
    todo = models.CharField(max_length=1000)
    created = models.DateField('created')
    due_date = models.DateField('task date')
    category = models.CharField(max_length=100)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.name
