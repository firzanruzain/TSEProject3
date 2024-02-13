from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from app import models

# Create your views here.

@login_required
def home(request):
    return render(
        request,
        'searcher-home.html'
    )

@login_required
def properties_shortlisted(request):
    # Retrieve shortlisted properties for the current searcher
    shortlisted_properties = models.ShortlistedProperty.objects.filter(searcher__user=request.user)
    return render(request, 'properties_shortlisted.html', {'shortlisted_properties': shortlisted_properties})

def property_search(request):
    properties = models.Property.objects.all()

    if request.method == 'GET':
        # Get search parameters from the request
        location = request.GET.get('location')
        min_price = request.GET.get('min_price')
        max_price = request.GET.get('max_price')
        bedrooms = request.GET.get('bedrooms')

        # Filter properties based on the search criteria
        if location:
            properties = properties.filter(location__icontains=location)
        if min_price:
            properties = properties.filter(price__gte=min_price)
        if max_price:
            properties = properties.filter(price__lte=max_price)
        if bedrooms:
            properties = properties.filter(bedrooms=bedrooms)

    return render(request, 'property_search.html', {'properties': properties})