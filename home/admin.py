from django.contrib import admin
from .models import HeroSection, Feature, Client, Statistic, Testimonial

@admin.register(HeroSection)
class HeroSectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'active', 'created_at', 'updated_at')
    list_filter = ('active',)
    search_fields = ('title', 'subtitle', 'description')
    ordering = ('-created_at',)

@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'created_at', 'updated_at')
    list_filter = ('created_at',)
    search_fields = ('title', 'description')
    ordering = ('order',)

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'active', 'order', 'created_at')
    list_filter = ('active',)
    search_fields = ('name',)
    ordering = ('order',)

@admin.register(Statistic)
class StatisticAdmin(admin.ModelAdmin):
    list_display = ('title', 'value', 'order', 'created_at')
    search_fields = ('title', 'value')
    ordering = ('order',)

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'client_company', 'rating', 'active', 'order')
    list_filter = ('active', 'rating')
    search_fields = ('client_name', 'client_company', 'content')
    ordering = ('order',)
