from django.shortcuts import render
from django.http import HttpResponse
import datetime

def helloworld(request):
    if request.method == 'GET':
        return HttpResponse('Hello world')

def goodbye(request):
    if request.method == 'GET':
        return HttpResponse('Good bye')

def nowdate(request):
    if request.method == 'GET':
        datetim = datetime.datetime.now()
        return HttpResponse(datetim)






