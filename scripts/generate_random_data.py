"""Script to generate random Companies and Fiscal Notes"""

import random
import datetime
from register.models import Company, FiscalNote
from register.validators import cnpj_calculate_second_digit, cnpj_calculate_first_digit


def generate_company_name(num):
    return "Company {0}".format(num)


def generate_company_cnpj():
    cnpj = "".join([str(random.randint(0, 9)) for _ in range(12)])
    cnpj = cnpj + str(cnpj_calculate_first_digit(cnpj))
    cnpj = cnpj + str(cnpj_calculate_second_digit(cnpj))
    cnpj = "{0}.{1}.{2}/{3}-{4}".format(cnpj[0:2], cnpj[2:5], cnpj[5:8], cnpj[8:12], cnpj[12:14])
    return cnpj


def generate_company(iter_num):
    name = generate_company_name(iter_num)
    cnpj = generate_company_cnpj()
    c = Company(cnpj=cnpj, name=name)
    c.save()
    return c


def generate_fiscalnote(iter_num, company):
    series = str(iter_num)
    number = random.randint(0, 1000)
    name_description = "FiscalNote Item {0}".format(iter_num)
    weight = round(random.random()*10000, 2)
    volume = round(random.random()*50, 2)
    date = datetime.datetime.now()
    fn = FiscalNote(company=company, series=series, number=number, name_description=name_description,
                    weight=weight, volume=volume, date=date)
    fn.save()
    return fn


for i in range(20):
    c = generate_company(i)
    print(c, "Created")
    for j in range(random.randint(20, 25)):
        fn = generate_fiscalnote(j, c)
        print(fn, "Created")

exit()
