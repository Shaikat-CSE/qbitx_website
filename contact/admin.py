from django.contrib import admin
from .models import ContactMessage, Office, ServiceRequest, Newsletter

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'status', 'created_at', 'days_since_created')
    list_filter = ('status', 'created_at', 'service_interest')
    search_fields = ('name', 'email', 'subject', 'message', 'company')
    readonly_fields = ('created_at', 'ip_address')
    ordering = ('-created_at',)
    date_hierarchy = 'created_at'
    actions = ['mark_as_completed', 'mark_as_in_progress', 'mark_as_spam']
    
    def mark_as_completed(self, request, queryset):
        queryset.update(status='completed')
    mark_as_completed.short_description = "Mark selected messages as completed"
    
    def mark_as_in_progress(self, request, queryset):
        queryset.update(status='in_progress')
    mark_as_in_progress.short_description = "Mark selected messages as in progress"
    
    def mark_as_spam(self, request, queryset):
        queryset.update(status='spam')
    mark_as_spam.short_description = "Mark selected messages as spam"

@admin.register(Office)
class OfficeAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone', 'is_headquarters', 'active', 'order')
    list_filter = ('is_headquarters', 'active')
    search_fields = ('name', 'address', 'phone', 'email')
    ordering = ('-is_headquarters', 'order')

@admin.register(ServiceRequest)
class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'service_type', 'company', 'status', 'created_at')
    list_filter = ('status', 'service_type', 'created_at')
    search_fields = ('name', 'email', 'company', 'project_description', 'notes')
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)
    date_hierarchy = 'created_at'
    actions = ['mark_as_contacted', 'mark_as_proposal_sent', 'mark_as_closed_won', 'mark_as_closed_lost']
    
    def mark_as_contacted(self, request, queryset):
        queryset.update(status='contacted')
    mark_as_contacted.short_description = "Mark selected requests as contacted"
    
    def mark_as_proposal_sent(self, request, queryset):
        queryset.update(status='proposal_sent')
    mark_as_proposal_sent.short_description = "Mark selected requests as proposal sent"
    
    def mark_as_closed_won(self, request, queryset):
        queryset.update(status='closed_won')
    mark_as_closed_won.short_description = "Mark selected requests as closed won"
    
    def mark_as_closed_lost(self, request, queryset):
        queryset.update(status='closed_lost')
    mark_as_closed_lost.short_description = "Mark selected requests as closed lost"

@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'is_active', 'subscribed_date')
    list_filter = ('is_active', 'subscribed_date')
    search_fields = ('email', 'name')
    ordering = ('-subscribed_date',)
    actions = ['activate_subscriptions', 'deactivate_subscriptions']
    
    def activate_subscriptions(self, request, queryset):
        queryset.update(is_active=True)
    activate_subscriptions.short_description = "Activate selected subscriptions"
    
    def deactivate_subscriptions(self, request, queryset):
        queryset.update(is_active=False)
    deactivate_subscriptions.short_description = "Deactivate selected subscriptions"
