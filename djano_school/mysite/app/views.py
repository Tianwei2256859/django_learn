# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from models import Student
import json
@csrf_exempt
def ajax_test_add(request):
    a = request.POST.get('a')
    print "="*32
    if a :
        return_json = list(Student.objects.filter(name__contains=a).values('name'))
    else:
        return_json = {}
    return HttpResponse(json.dumps(return_json), content_type='application/json')

def index(request):
    return render(request,'index.html')

