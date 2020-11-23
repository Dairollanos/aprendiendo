from django.shortcuts import render
from django.http import HttpResponse


def dashboard(request):
    return HttpResponse('<h1>loquesea pero la vacila</h1>')
