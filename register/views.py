from django.shortcuts import render, get_object_or_404, get_list_or_404
from register.models import Company, FiscalNote


def home(request):
    data = dict()
    data['companies'] = Company.objects.all()
    return render(request, "register/home.html", data)


def company_detail(request, id):
    data = dict()
    company = get_object_or_404(Company, id=id)
    data['company'] = company
    data['fiscal_notes'] = company.fiscalnote_set.all()
    return render(request, "register/company_detail.html", data)
