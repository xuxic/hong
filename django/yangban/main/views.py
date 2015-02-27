from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from main.models import Message, Vote

def index(request):
    context = {}
    return render(request, 'main/index.html', context)

def vote(request):
    v = Vote.objects.all()[0]
    if request.method == 'GET':
        return HttpResponse(v.count)
    elif request.method == 'POST':
        v.count += 1
        v.save()
        return HttpResponse(v.count)
    else:
        return HttpResponse(99999)