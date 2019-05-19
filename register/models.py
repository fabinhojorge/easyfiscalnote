from django.db import models
from register.validators import cnpj_validator


class Company(models.Model):
    name = models.CharField("Name", max_length=100)
    cnpj = models.CharField("CNPJ", validators=[cnpj_validator], max_length=18, unique=True)
    create_at = models.DateTimeField("Create at", auto_now_add=True)
    updated_at = models.DateTimeField("Update at", auto_now=True)

    def __str__(self):
        return "{0:03d} - {1}".format(self.id, self.name)

    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"
        ordering = ['id']


class FiscalNote(models.Model):
    company = models.ForeignKey(Company, verbose_name='Company', on_delete=models.CASCADE)
    series = models.CharField("Series", max_length=20, null=False)
    number = models.IntegerField('Number', default=0, null=False)
    name_description = models.TextField("Name/Description", blank=True)
    weight = models.FloatField('Weight', default=0)
    weight_metric = models.CharField("Weight Metric", blank=True, default='Kg', max_length=4)
    volume = models.FloatField('Volume', default=0)
    volume_metric = models.CharField("Volume Metric", blank=True, default='m3', max_length=4)
    date = models.DateField("Date", null=False)

    create_at = models.DateTimeField("Create at", auto_now_add=True)
    updated_at = models.DateTimeField("Update at", auto_now=True)

    def __str__(self):
        return "{0:03d} - {1}".format(self.id, self.name_description)

    class Meta:
        verbose_name = "FiscalNote"
        verbose_name_plural = "FiscalNotes"
        ordering = ['id']
