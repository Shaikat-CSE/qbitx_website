from django.contrib import admin
from .models import ServiceCategory, Service, ServiceFeature, ServiceFAQ

class ServiceFeatureInline(admin.TabularInline):
    model = ServiceFeature
    extra = 1

class ServiceFAQInline(admin.TabularInline):
    model = ServiceFAQ
    extra = 1

@admin.register(ServiceCategory)
class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'active', 'order', 'created_at')
    list_filter = ('active',)
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}
    ordering = ('order',)

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'featured', 'active', 'order')
    list_filter = ('featured', 'active', 'category')
    search_fields = ('name', 'short_description', 'full_description')
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ServiceFeatureInline, ServiceFAQInline]
    ordering = ('order',)

@admin.register(ServiceFeature)
class ServiceFeatureAdmin(admin.ModelAdmin):
    list_display = ('title', 'service', 'order')
    list_filter = ('service',)
    search_fields = ('title', 'description')
    ordering = ('service', 'order')

@admin.register(ServiceFAQ)
class ServiceFAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'service', 'order')
    list_filter = ('service',)
    search_fields = ('question', 'answer')
    ordering = ('service', 'order')
