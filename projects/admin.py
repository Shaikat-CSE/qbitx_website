from django.contrib import admin
from .models import ProjectCategory, Technology, Project, ProjectImage, ProjectTestimonial

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1

class ProjectTestimonialInline(admin.TabularInline):
    model = ProjectTestimonial
    extra = 0

@admin.register(ProjectCategory)
class ProjectCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'order')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}
    ordering = ('order', 'name')

@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    ordering = ('name',)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'client_name', 'status', 'featured', 'completion_date')
    list_filter = ('status', 'featured', 'category', 'technologies')
    search_fields = ('title', 'client_name', 'short_description', 'full_description')
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ('technologies',)
    inlines = [ProjectImageInline, ProjectTestimonialInline]
    ordering = ('-featured', 'order', '-completion_date')
    date_hierarchy = 'completion_date'

@admin.register(ProjectImage)
class ProjectImageAdmin(admin.ModelAdmin):
    list_display = ('project', 'title', 'order')
    list_filter = ('project',)
    search_fields = ('title', 'project__title')
    ordering = ('project', 'order')

@admin.register(ProjectTestimonial)
class ProjectTestimonialAdmin(admin.ModelAdmin):
    list_display = ('project', 'client_name', 'client_position', 'rating')
    list_filter = ('project', 'rating')
    search_fields = ('client_name', 'content', 'project__title')
    ordering = ('project', 'client_name')
