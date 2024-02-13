from django.urls import path
from Searcher import views

urlpatterns = [
    path('', views.home, name='home'),
    path('shortlisted/', views.properties_shortlisted, name='properties_shortlisted'),
    path('search/', views.property_search, name='properties_search'),
]