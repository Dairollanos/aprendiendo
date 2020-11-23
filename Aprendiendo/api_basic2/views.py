from django.shortcuts import render
from django.http import HttpResponse


def otrapagina(request):
    return HttpResponse('<h1>loquesea22</h1>')


def otrapagina2(request):
    return HttpResponse('<h1>loquesea33</h1>')


def otrapagina3(request):
    return HttpResponse('<h1>loquesea44</h1>')
