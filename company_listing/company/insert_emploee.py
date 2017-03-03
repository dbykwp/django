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


# +------------------+--------------+------+-----+---------+-------+
# | Field            | Type         | Null | Key | Default | Extra |
# +------------------+--------------+------+-----+---------+-------+
# | name             | varchar(100) | NO   |     | NULL    |       |
# | din              | varchar(20)  | NO   | PRI | NULL    |       |
# | designation      | varchar(20)  | NO   |     | NULL    |       |
# | appointment_date | date         | NO   |     | NULL    |       |
# | company_id       | varchar(30)  | NO   | MUL | NULL    |       |
# +------------------+--------------+------+-----+---------+-------+

class CompanyDetails(APIView):
#L01132WB1918PLC003029,ASHIT KUMAR SARKAR,Secretary,2014-11-01,ALDPS1750R
    def get(self, request, cid):
        company = Company.objects.get(pk=cid)
        data = CompanySerializer(company).data
        with open('/home/dheeraj/experiments/company/employee.csv', 'rb') as f:
            reader = csv.reader(f)
            for row in reader:
                if len(row) < 5:
                    print row
                    continue
                try:
                    company = Employee()
                    company.company_id = str(row[0])
                    company.name = str(row[1])
                    company.din = row[4]
                    company.designation = row[2]
                    company.appointment_date = datetime.strptime(row[3], "%Y-%m-%d").date() if row[3] !=  '' else None
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
