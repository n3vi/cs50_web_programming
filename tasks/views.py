from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse


class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")

# Create your views here.
def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []
    
    return render(request, "tasks/index.html",{
        "tasks": request.session["tasks"]
    })

def add(request):
    if request.method == "POST":    #we check if user submitted data
        form = NewTaskForm(request.POST)    #save submitted data if 'form' variable
        if form.is_valid(): #check if form provided all data in right format
            task = form.cleaned_data["task"]
            request.session["tasks"] += [task]
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            return render(request, "tasks/add.html", {
                "form": form    #pass in the form user submitted so the user can see errors and make modifications
            })
    return render(request, "tasks/add.html", {
        "form": NewTaskForm()   #if not POST but GET, show empty form to user
    })