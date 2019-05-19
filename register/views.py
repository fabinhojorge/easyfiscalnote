from django.shortcuts import render


def home(request):
    data = dict()
    return render(request, "register/home.html", data)
