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
    created = models.DateField('created')
    due_date = models.DateField('task date')
    category = models.CharField(max_length=100)
    done = models.BooleanField(default=False)

    # @classmethod
    # def create(cls, description, date, categ):
    #     todo = cls(due_date=date, name=description, category=categ)
    #     return todo

    def __str__(self):
        return self.name
