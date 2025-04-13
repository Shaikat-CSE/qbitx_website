from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import Http404

from .models import Service, ServiceCategory, ServiceFeature, ServiceFAQ
from contact.forms import ServiceRequestForm
from contact.models import ServiceRequest

def service_list(request):
    """View to display all services"""
    active_services = Service.objects.filter(active=True)
    categories = ServiceCategory.objects.filter(active=True)
    
    context = {
        'services': active_services,
        'categories': categories,
        'title': 'Our Services',
        'description': 'Explore our comprehensive range of software development and digital transformation services.'
    }
    return render(request, 'services/service_list.html', context)

def service_list_by_category(request, category_slug):
    """View to display services filtered by category"""
    category = get_object_or_404(ServiceCategory, slug=category_slug, active=True)
    services = Service.objects.filter(category=category, active=True)
    
    context = {
        'category': category,
        'services': services,
        'categories': ServiceCategory.objects.filter(active=True),
        'title': f'{category.name} Services',
        'description': category.description,
    }
    return render(request, 'services/service_list_by_category.html', context)

def service_detail(request, service_slug):
    """View to display service details"""
    service = get_object_or_404(Service, slug=service_slug, active=True)
    features = ServiceFeature.objects.filter(service=service)
    faqs = ServiceFAQ.objects.filter(service=service)
    related_services = Service.objects.filter(category=service.category, active=True).exclude(id=service.id)[:3]
    
    context = {
        'service': service,
        'features': features,
        'faqs': faqs,
        'related_services': related_services,
        'title': service.name,
        'description': service.short_description,
    }
    return render(request, 'services/service_detail.html', context)

def request_quote(request, service_slug):
    """View to request a quote for a specific service"""
    service = get_object_or_404(Service, slug=service_slug, active=True)
    
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.service_type = service.name
            service_request.save()
            messages.success(request, 'Your request has been submitted successfully. We will contact you shortly.')
            return redirect('services:service_detail', service_slug=service_slug)
    else:
        initial_data = {'service_type': service.name}
        form = ServiceRequestForm(initial=initial_data)
    
    context = {
        'form': form,
        'service': service,
        'title': f'Request Quote for {service.name}',
        'description': f'Fill out this form to request a quote for our {service.name} service.',
    }
    return render(request, 'services/request_quote.html', context)
