from django.shortcuts import HttpResponse
import time


#@router /second
def second(req):
    t = time.ctime()
    return HttpResponse(f'<h1>{t}</h1>')
