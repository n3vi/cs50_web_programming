from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    # return HttpResponse("Hello!")
    return render(request, "hello/index.html")

def luka(request):
    return HttpResponse("Hello, Luka :*** Love U!")

def marusia(request):
    return HttpResponse("Hello, Marusia :* Love U!")

def greet(request, name):
    # return HttpResponse(f"Hello, {name.capitalize()}")
    #3rd argument is a CONTEXT that I want to provide to the html template
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })