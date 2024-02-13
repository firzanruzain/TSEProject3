from django.urls import path
from Searcher import views

urlpatterns = [
    path('', views.home, name='home'),
    path('shortlisted/', views.properties_shortlisted, name='properties_shortlisted'),
    path('search/', views.property_search, name='properties_search'),
    path('add-to-shortlisted/<int:pk>/', views.property_add_to_shortlisted, name='property_add_to_shortlisted'),
    path('remove-from-shortlisted/<int:pk>/', views.property_remove_from_shortlisted, name='property_remove_from_shortlisted'),
]