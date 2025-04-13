from about.models import CompanyInfo
from contact.forms import NewsletterForm

def company_info(request):
    """Context processor to add company information to all templates"""
    try:
        info = CompanyInfo.objects.first()
    except:
        info = None
    
    return {
        'company_info': info,
        'newsletter_form': NewsletterForm(),
        'is_home': request.path == '/',
    }
