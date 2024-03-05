import random

from django.shortcuts import render
from django.http import HttpResponse

def models_list(request):
    random_number = random.randint(a=0, b=100)
    return HttpResponse(f"Vaše supr dupr náhodné čísílko je {random_number}")
def test_list(request):
    random_number = random.randint(a=0, b=100)
    return render(request, 'blog/test.html', {"random_number":random_number})

#vytvorit html temp do nej nacitat dyn data