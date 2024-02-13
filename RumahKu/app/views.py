from django.shortcuts import get_object_or_404, render, redirect

# Create your views here.
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Property, ApplicationRequest, InAppMessage, ShortlistedProperty

from django.contrib.auth.decorators import login_required

"""
def home(request):
    renders the home page.
    assert isinstance(request, HttpRequest)
    if request.user.is_authenticated:
        return(redirect('/menu'))
    else:
        return render(
            request,
            'app/index.html',
            {
                'title':'Home Page',
                'year': datetime.now().year,
            }
        )
"""
def home(request):
    user_group = request.user.groups.first().name.lower() if request.user.groups.exists() else None

    if request.user.groups.filter(name='Owner').exists():
        return redirect('owner/')
    if request.user.groups.filter(name='Searcher').exists():
        return redirect('searcher/')
    if request.user.groups.filter(name='Tenant').exists():
        return redirect('tenant/')
    else:
        return render(
            request,
            'app/index.html',
            {
                'title':'Home Page',
                'year': datetime.now().year,
            }
        ) # Default home view if user is not in any specific group

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Dr. Yeoh.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'ABC System',
            'message':'This application processes ...',
            'year':datetime.now().year,
        }
    )

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after registration
            return redirect('home')  # Redirect to the home page after registration
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


@login_required
def application_requests(request):
    application_requests = ApplicationRequest.objects.filter(searcher=request.user)
    return render(request, 'searcher/application_requests.html', {'application_requests': application_requests})

@login_required
def in_app_messages(request):
    messages = InAppMessage.objects.filter(receiver=request.user)
    return render(request, 'searcher/in_app_messages.html', {'messages': messages})

from .forms import PropertyUpdateForm


def property_detail(request, property_id):
    property = get_object_or_404(Property, pk=property_id)

    property_with_pictures = Property.objects.prefetch_related('pictures').get(pk=property_id)
    is_shortlisted = False
    if request.user.is_authenticated and request.user.groups.filter(name='Searcher').exists():
        # Check if the property is already in shortlisted properties for the current user
        is_shortlisted = ShortlistedProperty.objects.filter(property=property, searcher=request.user.searcher).exists()

    return render(request, 'app/property_detail.html', {'property': property, 'is_shortlisted': is_shortlisted})

@login_required
def property_create(request):
    if request.method == 'POST':
        form = PropertyUpdateForm(request.POST, request.FILES)
        if form.is_valid():
            property = form.save(commit=False)
            property.owner = request.user.owner  # Associate the property with the currently logged-in owner
            property.save()
            return redirect('home')
    else:
        form = PropertyUpdateForm()
    return render(request, 'Owner/property_create.html', {'form': form})