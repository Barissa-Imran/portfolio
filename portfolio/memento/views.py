from django import forms
from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Project
from .forms import ContactForm


def index(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Your message was sent successfully")
        else:
            return HttpResponse("Please try again")
    form = ContactForm()
    context = {"projects": Project.objects.all(), "form": form}
    return render(request, "index.html", context)
