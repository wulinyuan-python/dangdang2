from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    print('这是首页')
    return HttpResponse('hehe')

def login(request):
    print('giao')
    return HttpResponse('登陆')
