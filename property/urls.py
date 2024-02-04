# urls.py

from django.urls import path
from .views import (
    admin_register, admin_login, admin_logout,
    property_listing, create_property, property_profile,
    tenant_management, create_tenant, tenant_profile,create_unit,
    search
)
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/register/', admin_register, name='admin_register'),
    path('admin/login/', admin_login, name='admin_login'),
    path('admin/logout/', admin_logout, name='admin_logout'),

    path('property/listing/', property_listing, name='property_listing'),
    path('property/create/', create_property, name='create_property'),
    path('create-unit/<int:property_id>/', create_unit, name='create_unit'),
    path('property/profile/<int:property_id>/', property_profile, name='property_profile'),

    path('tenant/management/', tenant_management, name='tenant_management'),
    path('tenant/create/', create_tenant, name='create_tenant'),
    path('tenant/profile/<int:tenant_id>/', tenant_profile, name='tenant_profile'),
    path('search/', search, name='search'),
    path('', RedirectView.as_view(url='admin/login/')),
    # Add more paths as needed
]
