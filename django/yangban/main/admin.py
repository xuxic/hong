from django.contrib import admin

# Register your models here.
from main.models import Message, Vote

admin.site.register(Message)
admin.site.register(Vote)