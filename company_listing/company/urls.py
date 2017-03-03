from django.conf.urls import url

from . import views
app_name = 'company'

urlpatterns = [
    url(r'^companies/(?P<cin>[a-zA-Z0-9]+)/$', views.get_company, name='company_details'),
    url(r'^directorinfo/(?P<din>[a-zA-Z0-9]+)/$', views.get_director, name='employee_details'),
]