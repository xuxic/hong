from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.utils import timezone
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
    print request.method
    if request.method == 'GET':
        ret=[]
        for m in Message.objects.all():
            mm = {"email":m.email,"content":m.content,"pub_date":m.pub_date.ctime()}
            ret.append(mm)
        return HttpResponse(json.dumps(ret), content_type="application/json")
    elif request.method == 'POST':
        print request.body
        data = json.loads(request.body)
        m = Message(email=data["email"], content=data["content"], pub_date=timezone.now())
        m.save()
        ret = {"email":m.email, "content":m.content, "pub_date":m.pub_date.ctime()}
        return HttpResponse(json.dumps(ret), content_type="application/json")
    else:
        return HttpResponse(99999)
    