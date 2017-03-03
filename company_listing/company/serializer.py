from rest_framework import serializers
from models import Company, Employee


class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = ('name', 'din', 'designation', 'appointment_date')


class CompanySerializer(serializers.ModelSerializer):
    employee_set = EmployeeSerializer(many=True, read_only=True)
    # serializers.RelatedField(source='ProductImage', many=True)
    class Meta:
        model = Company
        fields = '__all__'
