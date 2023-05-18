from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return HttpResponse(u'Привет, мир!', content_type="text/plain")


def home_without_type(request):
    return HttpResponse(u'Привет, мир!')
