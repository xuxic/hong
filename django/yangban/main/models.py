from django.db import models

# Create your models here.
from django.db import models

class Message(models.Model):
    email = models.CharField(max_length=32)
    content = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):              # __unicode__ on Python 2
        return self.email

class Vote(models.Model):
    name = models.CharField(max_length=32)
    count = models.IntegerField(default=0)
    def __str__(self):              # __unicode__ on Python 2
        return self.name