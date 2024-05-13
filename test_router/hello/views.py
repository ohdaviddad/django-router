from django.shortcuts import HttpResponse

#@router /hello
def hello(request):
    return HttpResponse('Hello Django')

#@router /hello2
def hello2(request):
    return HttpResponse('Hello django-router')
