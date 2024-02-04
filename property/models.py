
# models.py

from django.db import models


class Property(models.Model):
    name = models.CharField(max_length=255, unique=True)
    address = models.TextField()
    location = models.CharField(max_length=255)
    features = models.TextField()

    def __str__(self):
        return self.name

class Unit(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    rent_cost = models.DecimalField(max_digits=10, decimal_places=2)
    bedroom_type = models.CharField(
        max_length=10,
        choices=[
            ('1BHK', '1 Bedroom, Hall, Kitchen'),
            ('2BHK', '2 Bedrooms, Hall, Kitchen'),
            ('3BHK', '3 Bedrooms, Hall, Kitchen'),
            ('4BHK', '4 Bedrooms, Hall, Kitchen'),
        ],
        default='1BHK'  # Set your desired default value here
    )

    def __str__(self):
        return f"{self.property.name} - {self.bedroom_type}"

class Tenant(models.Model):
    name = models.CharField(max_length=255, default='Default Name')
    address = models.TextField()
    document_proofs = models.TextField()

    def __str__(self):
        return self.name

class Lease(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    agreement_end_date = models.DateField()
    monthly_rent_date = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.tenant.name} - {self.unit.property.name} - {self.unit.bedroom_type}"
