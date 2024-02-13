from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from app import models
from django.forms import modelformset_factory
from app.forms import PropertyUpdateForm, PropertyPicturesForm
from django.shortcuts import get_object_or_404, render, redirect
# Create your views here.


@login_required
def properties(request):
    owner = request.user.owner
    properties = models.Property.objects.filter(owner=owner)
    return render(request, 'properties.html', {'properties': properties})

@login_required
def property_update(request, pk):
    property_obj = models.Property.objects.get(pk=pk)
    PropertyPicturesFormSet = modelformset_factory(models.PropertyPicture, form=PropertyPicturesForm, extra=1)

    if request.method == 'POST':
        property_form = PropertyUpdateForm(request.POST, instance=property_obj)
        pictures_formset = PropertyPicturesFormSet(request.POST, request.FILES, queryset=models.PropertyPicture.objects.filter(property=property_obj))
        if property_form.is_valid() and pictures_formset.is_valid():
            property_obj = property_form.save(commit=False)
            property_obj.save()

            # Save property pictures
            for form in pictures_formset:
                if form.cleaned_data:
                    picture = form.save(commit=False)
                    picture.property = property_obj
                    picture.save()

            return redirect('properties')
    else:
        property_form = PropertyUpdateForm(instance=property_obj)
        pictures_formset = PropertyPicturesFormSet(queryset=models.PropertyPicture.objects.filter(property=property_obj))

    return render(request, 'property_update.html', {'property_form': property_form, 'pictures_formset': pictures_formset})

@login_required
def home(request):
    return render(
        request,
        'owner-home.html'
    )