from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=50)
    weight = models.FloatField()
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField()

    def __str__(self):
        return self.name
