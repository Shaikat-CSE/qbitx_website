from django.contrib import admin
from .models import CompanyInfo, TeamMember, Milestone, FAQ

@admin.register(CompanyInfo)
class CompanyInfoAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'established_year', 'updated_at')
    search_fields = ('company_name', 'about_short', 'about_full')
    fieldsets = (
        (None, {
            'fields': ('company_name', 'tagline', 'logo', 'favicon', 'established_year')
        }),
        ('About Information', {
            'fields': ('about_short', 'about_full', 'mission', 'vision', 'values')
        }),
        ('Contact Information', {
            'fields': ('address', 'phone', 'email')
        }),
        ('Social Media', {
            'fields': ('facebook', 'twitter', 'linkedin', 'instagram', 'youtube', 'github')
        }),
    )

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'is_key_member', 'active', 'order')
    list_filter = ('is_key_member', 'active')
    search_fields = ('name', 'position', 'bio')
    ordering = ('order',)

@admin.register(Milestone)
class MilestoneAdmin(admin.ModelAdmin):
    list_display = ('year', 'title', 'order')
    search_fields = ('year', 'title', 'description')
    ordering = ('order', 'year')

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'category', 'active', 'order')
    list_filter = ('category', 'active')
    search_fields = ('question', 'answer', 'category')
    ordering = ('order',)
