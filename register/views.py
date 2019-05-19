from django.shortcuts import render
from register.models import Company


def home(request):
    data = dict()
    data['companies'] = Company.objects.all()
    return render(request, "register/home.html", data)
