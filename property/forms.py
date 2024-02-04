# forms.py

from django import forms
from .models import Property, Unit, Tenant, Lease

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['name', 'address', 'location', 'features']

class UnitForm(forms.ModelForm):
    class Meta:
        model = Unit
        fields = ['property','rent_cost', 'bedroom_type']

class TenantForm(forms.ModelForm):
    class Meta:
        model = Tenant
        fields = ['name', 'address', 'document_proofs']

class LeaseForm(forms.ModelForm):
    class Meta:
        model = Lease
        fields = [ 'unit', 'agreement_end_date', 'monthly_rent_date']

# You can use these forms to create, update, and validate data in your views.


from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','password1', 'password2')


