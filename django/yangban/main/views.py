from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from main.models import Message, Vote

import json

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
    
def mmmm(request):
    ret=[]
    print "hello"
    for m in Message.objects.all():
        print m
        mm = {"email":m.email,"content":m.content,"pub_date":m.pub_date.ctime()}
        ret.append(mm)
    print ret
    return HttpResponse(json.dumps(ret), content_type="application/json")