from django.shortcuts import render
from django.http import HttpResponse

def models_list(request):
    return HttpResponse("Testing of views")
