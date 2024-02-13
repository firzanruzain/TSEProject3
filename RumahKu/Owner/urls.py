from django.urls import path
from Owner import views

urlpatterns = [
    path('', views.home, name='home'),
    path('properties/', views.properties, name='properties'),
    path('property-update/<int:pk>', views.property_update, name='property_update'),
]