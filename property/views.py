
# views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import PropertyForm, UnitForm, TenantForm, LeaseForm, SignupForm
from .models import Property, Unit, Tenant, Lease

def admin_register(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('admin_login')
    else:
        form = SignupForm()

    return render(request, 'Auth/admin_register.html', {'form': form})


def admin_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('property_listing')  # Replace 'login' with your desired landing page
        else:
            # Handle authentication errors here, e.g., invalid credentials
            error_message = "Invalid username or password"
    else:
        error_message = None
    
    return render(request, 'Auth/admin_login.html', {'error_message': error_message})

def admin_logout(request):
    logout(request)
    return redirect('admin_login')


# views.py

from django.shortcuts import render, redirect
from .models import Property, Unit, Tenant, Lease
from .forms import PropertyForm, UnitForm, TenantForm, LeaseForm
from django.contrib.auth.decorators import login_required

@login_required(login_url='admin_login')
def property_listing(request):
    properties = Property.objects.all()
    return render(request, 'property_listing.html', {'properties': properties})

@login_required(login_url='admin_login')
def create_property(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST)
        if form.is_valid():
            property_instance = form.save()
            return redirect('property_profile', property_id=property_instance.id)
    else:
        form = PropertyForm()

    return render(request, 'create_property.html', {'form': form})

@login_required(login_url='admin_login')
def create_unit(request, property_id):
    property_instance = Property.objects.get(pk=property_id)

    if request.method == 'POST':
        form = UnitForm(request.POST)
        if form.is_valid():
            unit_instance = form.save(commit=False)
            unit_instance.property = property_instance
            unit_instance.save()
            return redirect('property_profile', property_id=property_id)
    else:
        form = UnitForm()

    return render(request, 'create_unit.html', {'property': property_instance, 'form': form})

@login_required(login_url='admin_login')
def property_profile(request, property_id):
    property_instance = Property.objects.get(pk=property_id)
    units = Unit.objects.filter(property=property_instance)
    leases = Lease.objects.filter(unit__property=property_instance)
    return render(request, 'property_profile.html', {'property': property_instance, 'units': units, 'leases': leases})

@login_required(login_url='admin_login')
def tenant_management(request):
    tenants = Tenant.objects.all()
    return render(request, 'tenant_management.html', {'tenants': tenants})

@login_required(login_url='admin_login')
def create_tenant(request):
    if request.method == 'POST':
        tenant_form = TenantForm(request.POST)
        lease_form = LeaseForm(request.POST)
        if tenant_form.is_valid() and lease_form.is_valid():
            tenant_instance = tenant_form.save()
            lease_form.instance.tenant = tenant_instance
            lease_form.save()
            return redirect('tenant_management')
    else:
        tenant_form = TenantForm()
        lease_form = LeaseForm()

    return render(request, 'create_tenant.html', {'tenant_form': tenant_form, 'lease_form': lease_form})

@login_required(login_url='admin_login')
def tenant_profile(request, tenant_id):
    tenant_instance = Tenant.objects.get(pk=tenant_id)
    leases = Lease.objects.filter(tenant=tenant_instance)
    return render(request, 'tenant_profile.html', {'tenant': tenant_instance, 'leases': leases})

from django.db.models import Q

@login_required(login_url='admin_login')
def search(request):
    query = request.GET.get('q', '')  # Get the search query from the URL parameter 'q'

    # Search for properties and units that start with the query
    properties = Property.objects.filter(name__startswith=query)
    units = Unit.objects.filter(Q(property__features__startswith=query) | Q(bedroom_type__startswith=query))

    context = {
        'query': query,
        'properties': properties,
        'units': units,
    }

    return render(request, 'search_results.html', context)




