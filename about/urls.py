from django.urls import path
from . import views

app_name = 'about'

urlpatterns = [
    path('', views.about, name='about'),
    path('team/', views.team, name='team'),
    path('faq/', views.faq, name='faq'),
]
