from django.contrib import admin

# Register your models here.
from .models import Employee, Company

admin.site.register(Employee)
admin.site.register(Company)
