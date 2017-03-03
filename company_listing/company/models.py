from __future__ import unicode_literals

from django.db import models
# Create your models here.

class Company(models.Model):
    Active = '1'
    Inactive = '0'
    STATUS_CHOICES = (
        (Active, 'Active'),
        (Inactive, 'Inactive')
    )
    identifier = models.CharField(max_length=30, primary_key=True)
    name = models.CharField(max_length=200)
    company_category = models.CharField(max_length=100)
    company_subcategory = models.CharField(max_length=100)
    company_type = models.CharField(max_length=100)
    authorized_capital = models.IntegerField()
    paidup_capital = models.IntegerField()
    incorporation_date = models.DateField()
    address_line1 = models.CharField(max_length=200, null=True)
    address_line2 = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    pincode = models.CharField(max_length=10)
    full_address = models.CharField(max_length=2000)
    agm_date = models.DateField(null=True)
    balance_sheet_date = models.DateField(null=True)
    status = models.CharField(choices=STATUS_CHOICES, default='Active', max_length=20)

    def __str__(self):
        return self.name

class Employee(models.Model):
    name = models.CharField(max_length=100)
    din = models.CharField(max_length=20, primary_key=True)
    designation = models.CharField(max_length=20)
    appointment_date = models.DateField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
