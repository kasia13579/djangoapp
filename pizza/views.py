from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    # return HttpResponse("<h1>Welcome to the django,</h1> we got fun n' games!")
    return render(request, 'pizza/index.html')


def komunikat(request):
    # return HttpResponse("We got everything you want, honey we know the name!")
    return render(request, 'pizza/komunikaty.html')


def robot(request):
    return HttpResponse("We are the people that can find, whatever you may need!")