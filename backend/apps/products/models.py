from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    CONDITION_CHOICES = [
        ('new', 'New'),
        ('used', 'Used'),
        ('worn', 'Worn'),
    ]
    condition = models.CharField(max_length=20, choices=CONDITION_CHOICES)
    
    def __str__(self):
        return self.name