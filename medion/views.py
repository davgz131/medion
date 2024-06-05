from django.http import HttpResponse
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render


def indexFuncion(request):

    return render(request,"index.html")

def indexFuncion2(request):

    return render(request,"index.html")

def page2(request):

    return render(request,"login.html")

def page3(request):

    return render(request,"mainPage.html")

def page4(request):

    return render(request,"login.html") 

def page5(request):

    return render(request,"about.html")

def page6(request):

    return render(request,"contact.html")