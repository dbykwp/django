from django.http import HttpResponse
from .models import Company, Employee
from django.core.exceptions import ObjectDoesNotExist
from django.core import serializers
import json

def get_signatories_for_company(cin):
    '''This function return list of emplyees in given company(cin)'''
    signatories = Employee.objects.filter(company_id=cin)
    data = serializers.serialize('json', signatories)
    signatories_list = []
    for emp in json.loads(data):
        signatory = emp['fields']
        signatory['din'] = emp['pk']
        signatories_list.append(signatory)
    return signatories_list

def get_company_json(cin, company):
    '''return json containing company details and list of signatories'''
    signatories = get_signatories_for_company(cin)
    data = serializers.serialize('json', [company])
    json_data = {'details': json.loads(data)[0]['fields']}
    json_data['signatories'] = signatories
    return json_data

def get_company(request, cin):
    ''' function called by urls to get company details'''
    try:
        company = Company.objects.get(pk=cin)
        json_data = get_company_json(cin, company)
    except ObjectDoesNotExist:
        json_data = {
            'error': {
                    'cin': cin,
                    'error': 'Company with given identifier does not exist in our database'
                }
            }
    return HttpResponse(json.dumps(json_data), content_type='application/json')

def get_director(request, din):
    ''' function called by urls to get signatories details'''
    try:
        employee = Employee.objects.get(pk=din)
        data = serializers.serialize('json', [employee])
        employee_detail = json.loads(data)[0]
        json_data = employee_detail['fields']
        json_data['din'] = employee_detail['pk']
    except ObjectDoesNotExist:
        json_data = {
            'error': {
                    'din': din,
                    'error': 'signatory with given din does not exist in our database'
                }
            } 
    return HttpResponse(json.dumps(json_data), content_type='application/json')
