from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Project, ProjectCategory, Technology, ProjectImage, ProjectTestimonial

def project_list(request):
    """View to display all projects"""
    projects_list = Project.objects.all()
    categories = ProjectCategory.objects.all()
    technologies = Technology.objects.all()
    
    # Filtering
    category_id = request.GET.get('category')
    technology_id = request.GET.get('technology')
    
    if category_id:
        projects_list = projects_list.filter(category_id=category_id)
    
    if technology_id:
        projects_list = projects_list.filter(technologies__id=technology_id)
    
    # Pagination
    paginator = Paginator(projects_list, 9)  # 9 projects per page
    page = request.GET.get('page')
    
    try:
        projects = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page
        projects = paginator.page(1)
    except EmptyPage:
        # If page is out of range, deliver last page of results
        projects = paginator.page(paginator.num_pages)
    
    context = {
        'projects': projects,
        'categories': categories,
        'technologies': technologies,
        'selected_category_id': int(category_id) if category_id else None,
        'selected_technology_id': int(technology_id) if technology_id else None,
        'title': 'Our Projects',
        'description': 'Explore our portfolio of successful projects across various industries.',
    }
    return render(request, 'projects/project_list.html', context)

def project_list_by_category(request, category_slug):
    """View to display projects filtered by category"""
    category = get_object_or_404(ProjectCategory, slug=category_slug)
    projects_list = Project.objects.filter(category=category)
    
    # Pagination
    paginator = Paginator(projects_list, 9)  # 9 projects per page
    page = request.GET.get('page')
    
    try:
        projects = paginator.page(page)
    except PageNotAnInteger:
        projects = paginator.page(1)
    except EmptyPage:
        projects = paginator.page(paginator.num_pages)
    
    context = {
        'category': category,
        'projects': projects,
        'categories': ProjectCategory.objects.all(),
        'technologies': Technology.objects.all(),
        'title': f'{category.name} Projects',
        'description': category.description,
    }
    return render(request, 'projects/project_list_by_category.html', context)

def project_list_by_technology(request, technology_slug):
    """View to display projects filtered by technology"""
    technology = get_object_or_404(Technology, slug=technology_slug)
    projects_list = Project.objects.filter(technologies=technology)
    
    # Pagination
    paginator = Paginator(projects_list, 9)  # 9 projects per page
    page = request.GET.get('page')
    
    try:
        projects = paginator.page(page)
    except PageNotAnInteger:
        projects = paginator.page(1)
    except EmptyPage:
        projects = paginator.page(paginator.num_pages)
    
    context = {
        'technology': technology,
        'projects': projects,
        'categories': ProjectCategory.objects.all(),
        'technologies': Technology.objects.all(),
        'title': f'Projects Using {technology.name}',
        'description': f'Explore our portfolio of projects built with {technology.name} technology.',
    }
    return render(request, 'projects/project_list_by_technology.html', context)

def project_detail(request, project_slug):
    """View to display project details"""
    project = get_object_or_404(Project, slug=project_slug)
    images = ProjectImage.objects.filter(project=project)
    testimonials = ProjectTestimonial.objects.filter(project=project)
    related_projects = Project.objects.filter(category=project.category).exclude(id=project.id)[:3]
    
    context = {
        'project': project,
        'images': images,
        'testimonials': testimonials,
        'related_projects': related_projects,
        'title': project.title,
        'description': project.short_description,
    }
    return render(request, 'projects/project_detail.html', context)
