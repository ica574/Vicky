from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, "homepage.html")

    #return HttpResponse("Vicky says 'nice!'")
def ask(request):
    return render(request, "ask.html")