from django.urls import path
from . import views

app_name = 'contact'

urlpatterns = [
    path('', views.contact, name='contact'),
    path('submit/', views.contact_submit, name='contact_submit'),
    path('service-request/', views.service_request, name='service_request'),
    path('service-request/submit/', views.service_request_submit, name='service_request_submit'),
]
