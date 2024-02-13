from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from app import models
from django.shortcuts import redirect, get_object_or_404

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

@login_required
def property_add_to_shortlisted(request, pk):
    if request.method == 'POST' and request.user.is_authenticated and request.user.groups.filter(name='Searcher').exists():
        property_obj = get_object_or_404(models.Property, id=pk)
        searcher_obj = request.user.searcher
        # Check if the property is not already in the shortlisted properties for the current searcher
        if not models.ShortlistedProperty.objects.filter(property=property_obj, searcher=searcher_obj).exists():
            # Add the property to the shortlisted list
            shortlisted_property = models.ShortlistedProperty(property=property_obj, searcher=searcher_obj)
            shortlisted_property.save()

    # Redirect back to the property detail page
    return redirect('property_detail', property_id=pk)

@login_required
def property_remove_from_shortlisted(request, pk):
    if request.method == 'POST' and request.user.is_authenticated and request.user.groups.filter(name='Searcher').exists():
        property_obj = get_object_or_404(models.Property, id=pk)
        searcher_obj = request.user.searcher
        # Check if the property is in the shortlisted properties for the current searcher
        shortlisted_property = models.ShortlistedProperty.objects.filter(property=property_obj, searcher=searcher_obj).first()
        if shortlisted_property:
            # Remove the property from the shortlisted list
            shortlisted_property.delete()

    # Redirect back to the property detail page
    return redirect('property_detail', property_id=pk)

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