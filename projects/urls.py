from django.urls import path
from . import views

app_name = 'projects'

urlpatterns = [
    path('', views.project_list, name='project_list'),
    path('category/<slug:category_slug>/', views.project_list_by_category, name='project_list_by_category'),
    path('technology/<slug:technology_slug>/', views.project_list_by_technology, name='project_list_by_technology'),
    path('<slug:project_slug>/', views.project_detail, name='project_detail'),
]
