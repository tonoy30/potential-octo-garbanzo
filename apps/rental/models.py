from django.db import models


# Product Models
class Product(models.Model):
    _PRODUCT_TYPE = (
        ('plain', 'Plain'),
        ('meter', 'Meter'),
    )
    _id = models.AutoField(primary_key=True, editable=False, db_index=True)
    code = models.CharField(max_length=2)
    name = models.CharField(max_length=450, blank=False, db_index=True)
    type = models.CharField(choices=_PRODUCT_TYPE,
                            default='plain', max_length=5, db_index=True)
    availability = models.BooleanField(default=True)
    needing_repair = models.BooleanField(default=False)
    durability = models.PositiveIntegerField(default=0, null=False)
    max_durability = models.PositiveIntegerField(default=0, null=False)
    mileage = models.PositiveIntegerField(default=None, null=True, blank=True)
    price = models.DecimalField(
        max_digits=15, decimal_places=1, default=0.0)
    minimum_rent_period = models.PositiveSmallIntegerField(
        default=1, null=False, blank=False)
    rented_at = models.DateTimeField(blank=True, null=True, editable=False)
    returned_at = models.DateTimeField(
        blank=True, null=True, editable=False)
    discount = models.FloatField(
        default=0, null=False, blank=False)

    def __str__(self) -> str:
        return f"{self.name} - {self.type}"
