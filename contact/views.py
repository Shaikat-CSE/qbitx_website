from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_POST

from .models import Office, ContactMessage, ServiceRequest
from .forms import ContactForm, ServiceRequestForm
from about.models import CompanyInfo

def contact(request):
    """View for the Contact Us page"""
    offices = Office.objects.filter(active=True)
    company_info = CompanyInfo.objects.first()
    form = ContactForm()
    
    context = {
        'offices': offices,
        'company_info': company_info,
        'form': form,
        'title': 'Contact Us',
        'description': 'Get in touch with QBITX Solutions. Contact us for any queries or services.',
    }
    return render(request, 'contact/contact.html', context)

@require_POST
def contact_submit(request):
    """Handle contact form submission"""
    if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_message = form.save(commit=False)
            contact_message.ip_address = request.META.get('REMOTE_ADDR')
            contact_message.save()
            return JsonResponse({
                'status': 'success',
                'message': 'Thank you for your message! We will get back to you shortly.'
            })
        else:
            errors = {field: form.errors[field][0] for field in form.errors}
            return JsonResponse({'status': 'error', 'errors': errors})
    else:
        # Handle non-AJAX POST request
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_message = form.save(commit=False)
            contact_message.ip_address = request.META.get('REMOTE_ADDR')
            contact_message.save()
            messages.success(request, 'Thank you for your message! We will get back to you shortly.')
        else:
            for field in form.errors:
                messages.error(request, form.errors[field][0])
        
        return redirect('contact:contact')

def service_request(request):
    """View for the Service Request page"""
    form = ServiceRequestForm()
    company_info = CompanyInfo.objects.first()
    
    context = {
        'form': form,
        'company_info': company_info,
        'title': 'Request a Service',
        'description': 'Request a custom service from QBITX Solutions. Tell us about your project requirements.',
    }
    return render(request, 'contact/service_request.html', context)

@require_POST
def service_request_submit(request):
    """Handle service request form submission"""
    if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        form = ServiceRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({
                'status': 'success',
                'message': 'Your service request has been submitted successfully. We will contact you shortly.'
            })
        else:
            errors = {field: form.errors[field][0] for field in form.errors}
            return JsonResponse({'status': 'error', 'errors': errors})
    else:
        # Handle non-AJAX POST request
        form = ServiceRequestForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your service request has been submitted successfully. We will contact you shortly.')
        else:
            for field in form.errors:
                messages.error(request, form.errors[field][0])
        
        return redirect('contact:service_request')
