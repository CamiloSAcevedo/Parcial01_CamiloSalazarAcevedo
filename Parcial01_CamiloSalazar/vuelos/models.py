from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.

class Flight(models.Model):
    NACIONAL = 'Nacional'
    INTERNACIONAL = 'Internacional'
    Type_Choices = [
        (NACIONAL, 'Nacional'),
        (INTERNACIONAL, 'Internacional'),

    ]

    name = models.CharField(max_length=50)
    type = models.CharField( max_length=30, choices=Type_Choices)
    price = models.DecimalField(max_digits=15, decimal_places=2, validators=[MinValueValidator(0)])

    def __str__(self):
        return f'{self.name} ({self.type}) - ${self.price}'