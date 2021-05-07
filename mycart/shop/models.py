from django.db import models

# Create model here
from django.db import models

class Product(models.Model):
    product_id=models.AutoField
    product_code=models.CharField(max_length=50)
    name=models.CharField(max_length=300)
    price=models.FloatField()

    def __str__(self):
        return self.name