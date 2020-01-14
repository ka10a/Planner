from django.db import models


from django.db import models

class Event(models.Model):
    date = models.DateTimeField('event date')
    name = models.CharField(max_length=200)

    def str(self):
        return self.name

class Calendar(models.Model):
    name = models.CharField(max_length=200)

    def str(self):
        return self.name
