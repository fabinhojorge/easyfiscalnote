from django.shortcuts import render, get_object_or_404, get_list_or_404
from register.models import Company, FiscalNote
from django.db.models import Q


def home(request):
    data = dict()
    data['companies'] = Company.objects.all()
    return render(request, "register/home.html", data)


def company_detail(request, id):
    data = dict()
    company = get_object_or_404(Company, id=id)
    data['company'] = company

    search = request.GET.get('search')
    if request.method == 'GET' and search:
        data['fiscal_notes'] = company.fiscalnote_set.filter(Q(series__contains=search) | Q(name_description__contains=search))
    else:
        data['fiscal_notes'] = company.fiscalnote_set.all()

    return render(request, "register/company_detail.html", data)
