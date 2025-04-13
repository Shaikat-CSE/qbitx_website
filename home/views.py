from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_POST

from .models import HeroSection, Feature, Client, Statistic, Testimonial
from services.models import Service, ServiceCategory
from projects.models import Project
from contact.models import Newsletter
from contact.forms import NewsletterForm

def home_view(request):
    """View for the home page"""
    context = {
        'hero': HeroSection.objects.filter(active=True).first(),
        'features': Feature.objects.all()[:6],
        'clients': Client.objects.filter(active=True)[:8],
        'statistics': Statistic.objects.all()[:4],
        'testimonials': Testimonial.objects.filter(active=True)[:6],
        'featured_services': Service.objects.filter(featured=True, active=True)[:6],
        'service_categories': ServiceCategory.objects.filter(active=True),
        'featured_projects': Project.objects.filter(featured=True)[:3],
        'newsletter_form': NewsletterForm(),
    }
    return render(request, 'home/index.html', context)

@require_POST
def newsletter_subscription(request):
    """Handle newsletter subscription"""
    if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            # Check if this email already exists
            if Newsletter.objects.filter(email=email).exists():
                # If inactive, reactivate it
                newsletter = Newsletter.objects.get(email=email)
                if not newsletter.is_active:
                    newsletter.is_active = True
                    newsletter.name = form.cleaned_data.get('name', '')
                    newsletter.save()
                    return JsonResponse({'status': 'success', 'message': 'Your subscription has been reactivated.'})
                else:
                    return JsonResponse({'status': 'info', 'message': 'You are already subscribed to our newsletter.'})
            else:
                # New subscription
                form.save()
                return JsonResponse({'status': 'success', 'message': 'Thank you for subscribing to our newsletter!'})
        else:
            # Form validation errors
            errors = {field: form.errors[field][0] for field in form.errors}
            return JsonResponse({'status': 'error', 'errors': errors})
    else:
        # Handle non-AJAX POST request
        form = NewsletterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            if Newsletter.objects.filter(email=email).exists():
                newsletter = Newsletter.objects.get(email=email)
                if not newsletter.is_active:
                    newsletter.is_active = True
                    newsletter.name = form.cleaned_data.get('name', '')
                    newsletter.save()
                    messages.success(request, 'Your subscription has been reactivated.')
                else:
                    messages.info(request, 'You are already subscribed to our newsletter.')
            else:
                form.save()
                messages.success(request, 'Thank you for subscribing to our newsletter!')
        else:
            for field in form.errors:
                messages.error(request, form.errors[field][0])
        
        # Redirect back to the referrer or home
        redirect_to = request.META.get('HTTP_REFERER', '/')
        return redirect(redirect_to)
