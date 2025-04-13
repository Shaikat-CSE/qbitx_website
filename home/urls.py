from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('subscribe-newsletter/', views.newsletter_subscription, name='newsletter_subscription'),
] 