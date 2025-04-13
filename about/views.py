from django.shortcuts import render

from .models import CompanyInfo, TeamMember, Milestone, FAQ

def about(request):
    """View for the About Us page"""
    company_info = CompanyInfo.objects.first()
    milestones = Milestone.objects.all()
    key_team_members = TeamMember.objects.filter(is_key_member=True, active=True)[:4]
    
    context = {
        'company_info': company_info,
        'milestones': milestones,
        'key_team_members': key_team_members,
        'title': 'About QBITX Solutions',
        'description': company_info.about_short if company_info else 'Learn more about QBITX Solutions, our mission, vision, and values.',
    }
    return render(request, 'about/about.html', context)

def team(request):
    """View for the Team page"""
    team_members = TeamMember.objects.filter(active=True)
    key_members = team_members.filter(is_key_member=True)
    other_members = team_members.filter(is_key_member=False)
    company_info = CompanyInfo.objects.first()
    
    context = {
        'key_members': key_members,
        'other_members': other_members,
        'company_info': company_info,
        'title': 'Our Team',
        'description': 'Meet the talented team behind QBITX Solutions.',
    }
    return render(request, 'about/team.html', context)

def faq(request):
    """View for the FAQ page"""
    faqs = FAQ.objects.filter(active=True)
    
    # Group FAQ by category
    categories = {}
    uncategorized = []
    
    for faq in faqs:
        if faq.category:
            if faq.category not in categories:
                categories[faq.category] = []
            categories[faq.category].append(faq)
        else:
            uncategorized.append(faq)
    
    context = {
        'categories': categories,
        'uncategorized': uncategorized,
        'title': 'Frequently Asked Questions',
        'description': 'Find answers to frequently asked questions about QBITX Solutions services.',
    }
    return render(request, 'about/faq.html', context)
