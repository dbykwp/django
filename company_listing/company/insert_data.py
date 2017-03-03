from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .serializer import CompanySerializer, EmployeeSerializer
from rest_framework.views import APIView
from .models import Company, Employee
from rest_framework import status
from rest_framework.response import Response
#from django.views.decorators.csrf import csrf_token
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
# Create your views here.
import csv
import MySQLdb
from datetime import datetime

class CompanyList(APIView):

    def get(self, request):
        company = Company.objects.all()
        data = CompanySerializer(company, many=True).data
        return Response(data)

class CompanyDetails(APIView):

    def get(self, request, cid):
        company = Company.objects.get(pk=cid)
        data = CompanySerializer(company).data
        with open('/home/dheeraj/experiments/company/company_data.csv', 'rb') as f:
            reader = csv.reader(f)
            for row in reader:
                try:
                    company = Company()
                    company.identifier = str(row[0])
                    company.name = str(row[1])
                    company.company_category = row[2]
                    company.company_subcategory = row[3]
                    company.company_type = row[4]
                    company.authorized_capital = int(row[5])
                    company.paidup_capital = int(row[6])
                    company.incorporation_date = datetime.strptime(row[7], "%Y-%m-%d").date() if row[7] !=  '' else None
                    company.address_line1 = row[8]
                    company.address_line2 = row[9]
                    company.city = row[10]
                    company.state = row[11]
                    company.country = row[12]
                    company.pincode = row[13]
                    company.full_address = row[14]
                    company.agm_date = datetime.strptime(row[15], "%Y-%m-%d").date() if row[15] !=  '' else None
                    company.balance_sheet_date = datetime.strptime(row[16], "%Y-%m-%d").date() if row[16] !=  '' else None
                    company.status = row[17]
                    company.save()
                except Exception as e:
                    print row
                    print e
        return Response(data)

class EmployeeDetails(APIView):

    def get(self, request, din):
        employee = Employee.objects.get(pk=din)
        data = EmployeeSerializer(employee).data
        return Response(data)
