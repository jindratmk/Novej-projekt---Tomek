import random

from django.shortcuts import render
from django.http import HttpResponse

def models_list(request):
    random_number = random.randint(a=0, b=100)
    return HttpResponse(f"Random number{random_number}")
